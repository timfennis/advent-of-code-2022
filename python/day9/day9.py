lines = [line for line in open('input').read().split('\n')]

dirs = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

def clamp(i: int) -> int:
    if i in [1, 2]:
        return 1
    elif i in [-1, -2]:
        return -1
    elif i == 0:
        return 0
    else:
        raise ValueError(f"unexpected {i}")

def simulate(lines: list[str], snek_len: int):
    rope = [(0, 0) for _ in range(snek_len)]
    visited = set([(0, 0)])
    for line in lines:
        direction = line[0]
        n_steps = int(line[1:])

        for _ in range(n_steps):
            dx, dy = dirs[direction]
            rope[0] = (rope[0][0] + dx, rope[0][1] + dy)

            for idx in range(1, len(rope)):
                dx = rope[idx-1][0] - rope[idx][0]
                dy = rope[idx-1][1] - rope[idx][1]

                if abs(dx) in [1,0] and abs(dy) in [1,0]:
                    pass # do nothing
                else:
                    rope[idx] = (rope[idx][0] + clamp(dx), rope[idx][1] + clamp(dy))
                
            visited.add(rope[-1])
    return visited   

p1 = len(set(simulate(lines, 2)))
p2 = len(set(simulate(lines, 10)))
print(p1, p2, sep="\n")
assert p1 == 6284
assert p2 == 2661
print(p1, p2, sep="\n")
