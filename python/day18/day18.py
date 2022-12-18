from collections import defaultdict
import sys

sys.setrecursionlimit(10_000)

input = open('input').read()

drops = set()
for line in input.split('\n'):
    x, y, z = line.split(',')
    drops.add((int(x), int(y), int(z)))


minx = min([x for x, _, _ in drops])
maxx = max([x for x, _, _ in drops])
miny = min([y for _, y, _ in drops])
maxy = max([y for _, y, _ in drops])
minz = min([z for _, _, z in drops])
maxz = max([z for _, _, z in drops])

print(f"x from {minx} to {maxx}")
print(f"y from {miny} to {maxy}")
print(f"z from {minz} to {maxz}")


def in_bounds(d):
    return d[0] in range(minx, maxx+1) and d[1] in range(miny, maxy+1) and d[2] in range(minz, maxz+1)
def in_bounds2(d):
    return d[0] in range(0, maxx+1) and d[1] in range(0, maxy+1) and d[2] in range(0, maxz+1)

def neighbours(d):
    x, y, z = d
    yield (x-1, y, z)
    yield (x+1, y, z)
    yield (x, y-1, z)
    yield (x, y+1, z)
    yield (x, y, z-1)
    yield (x, y, z+1)

G = defaultdict(lambda: None)

def flood_fill(x,y,z):
    p = (x,y,z)

    # If we've already visited this node just return the answer
    if G[p] != None:
        return G[p]

    # If the current node contains a drop, mark this block as not connected
    # and abort the search
    if p in drops:
        G[p] = False
        # Abort don't continue searching
        return

    G[p] = True 
    for n in neighbours(p):
        if not in_bounds2(n): continue
        if G[n] == None:
            flood_fill(n[0], n[1], n[2])

flood_fill(0,0,0)

for z in range(minz, maxz+1):
    for y in range(miny, maxy+1):
        print(''.join([' ' if G[x,y,z] == True else '#' for x in range(minx,maxx+1)]))
    print(''.join('-' for _ in range(21)))

def exposed_sides(d):
    exposed = 6
    for n in neighbours(d):
        if n in drops:
            exposed -= 1
    
    return exposed


def exposed_sides2(d, seen = set()):

    exposed = 0

    for n in neighbours(d):
        if G[n] == True:
            exposed += 1
        elif not in_bounds(n):
            exposed += 1

    return exposed


total = 0
total2 = 0
for drop in drops:
    total += exposed_sides(drop)
    total2 += exposed_sides2(drop)

print(total)
print(total2)

