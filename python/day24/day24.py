from copy import deepcopy
from collections import deque, defaultdict
import functools

data = open('input').read()
# data = open('example').read()

WALLS = set()
INITIAL_BLIZZ = set()
for row, line in enumerate(data.splitlines()):
    for col, c in enumerate(line):
        if c in ['>', 'v', '<', '^']:
            INITIAL_BLIZZ.add((row, col, c))
        elif c == '#':
            WALLS.add((row, col))

INITIAL_BLIZZ = frozenset(INITIAL_BLIZZ)
WALLS = frozenset(WALLS)

# Todo find automatically
max_r = max([r for r, c in WALLS])
max_c = max([c for r, c in WALLS])
start, end = (0, 1), (max_r, max_c - 1)

def print_grid(blizz, walls, you = None):
    buf = ''
    blizz_map = defaultdict(int)

    for b in blizz:
        a, b, c = b
        if (a, b) in blizz_map:
            d = blizz_map[a, b]
            if isinstance(d, int):
                blizz_map[a, b] = blizz_map[a, b] + 1
            else:
                blizz_map[a, b] = 2
        else:
            blizz_map[a, b] = c

    for r in range(0, max_r + 1):
        for c in range(0, max_c + 1):
            if (r,c) == you:
                buf += 'E'
            elif (r,c) in walls:
                buf += '#'
            elif (r,c) in blizz_map:
                buf += str(blizz_map[r, c])
            else:
                buf += '.'
        buf += '\n'

    print(buf, end="")

def blizz_dir(c):
    if c == '>':
        return (0, 1)
    elif c == '<':
        return (0, -1)
    elif c == '^':
        return (-1, 0)
    elif c == 'v':
        return (1, 0)

@functools.lru_cache(maxsize=None)
def next_blizz(blizz: frozenset, walls: frozenset):
    next_blizz = set()
    for cr, cc, obj in blizz:
        dr, dc = blizz_dir(obj)
        nr, nc = cr + dr, cc + dc

        if (nr, nc) in walls:
            if obj == 'v':
                nr = 1
            elif obj == '<':
                nc = max_c - 1
            elif obj == '>':
                nc = 1
            elif obj == '^':
                nr = max_r - 1 

        next_blizz.add((nr, nc, obj))
        
    return frozenset(next_blizz)

def intersect(b, w):
    out = set()
    for r, c, _ in b:
        out.add((r, c))
    for r, c in w:
        out.add((r, c))
    return out

BLIZZ_CACHE = dict()
BLIZZ_CACHE[0] = INITIAL_BLIZZ

def blizz_at_time(time):
    # Mod trick to speed things up slightly
    time = time % (600 if len(data) == 3320 else 12)
    start_time = max([t for t in BLIZZ_CACHE.keys() if t <= time])
    cur = BLIZZ_CACHE[start_time]
    for dt in range(1, time-start_time + 1):
        cur = next_blizz(cur, WALLS)
        BLIZZ_CACHE[start_time + dt] = cur
    return cur

def bfs(start, end, repeat = 0, time = 1):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
    queue = deque()
    queue.append(start + (time,))
    seen = set()

    while len(queue) > 0:
        cr, cc, time = queue.popleft()
        blizz = blizz_at_time(time)
        
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            if nr < 0: continue
            if any(nr == r and nc == c for r, c, _ in blizz): continue
            if (nr, nc) in WALLS: continue
            if (nr, nc) == end and repeat == 0: return time
            if (nr, nc) == end and repeat > 0:
                seen.clear()
                print('Intermediate', time)
                return bfs(end, start, repeat - 1, time + 1)
            if (nr, nc, time + 1) in seen: continue

            seen.add((nr, nc, time + 1))

            queue.append((nr, nc, time + 1))

print(start, end)
print(bfs(start, end, 2)) 