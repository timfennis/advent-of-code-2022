lines = [line for line in open('input').read().split('\n')]
dirs = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)

rope = [(0, 0) for _ in range(10)]
visited = [set() for _ in range(10)]

for line in lines:
    direction, n_steps = line.split()

    for _ in range(int(n_steps)):
        dx, dy = dirs[direction]
        rope[0] = (rope[0][0] + dx, rope[0][1] + dy)

        for idx in range(1, len(rope)):
            dx, dy = rope[idx-1][0] - rope[idx][0], rope[idx-1][1] - rope[idx][1]

            # if chebyshev distance is less than 2 we can stay where we are
            if max(abs(dx),abs(dy)) > 1: 
                rope[idx] = (rope[idx][0] + sign(dx), rope[idx][1] + sign(dy))
            visited[idx].add(rope[idx])

R = [len(s) for s in visited]
assert R[1] == 6284
assert R[9] == 2661
print(R[1], R[9], sep="\n")
