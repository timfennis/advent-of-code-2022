lines = [line for line in open('input').read().split('\n')]

def clamp(i: int) -> int:
    if i == 2 or i == 1:
        return 1
    elif i == -2 or i == -1:
        return -1
    elif i == 0:
        return 0
    else:
        print("PANIC", i)
        exit()
def simulate(lines: list[str], snek_len: int):
    rope = [(0, 0) for _ in range(snek_len)]
    visited = set([(0, 0)])
    for line in lines:
        direction = line[0]
        n_steps = int(line[1:])

        for _ in range(n_steps):
            if direction == 'U':
                rope[0] = (rope[0][0], rope[0][1]+1)
            elif direction == 'D':
                rope[0] = (rope[0][0], rope[0][1]-1)
            elif direction == 'L':
                rope[0] = (rope[0][0] - 1, rope[0][1])
            elif direction == 'R':
                rope[0] = (rope[0][0] + 1, rope[0][1])

            for idx in range(1, len(rope)):
                dx = rope[idx-1][0] - rope[idx][0]
                dy = rope[idx-1][1] - rope[idx][1]

                if abs(dx) in [1,0] and abs(dy) in [1,0]:
                    # do nothing 
                    continue
                else:
                    dx = clamp(dx)
                    dy = clamp(dy) 
                
                rope[idx] = (rope[idx][0] + dx, rope[idx][1] + dy)
                
                if idx == len(rope) - 1:
                    visited.add((rope[idx][0], rope[idx][1]))
    return visited   

p1 = len(set(simulate(lines, 2)))
p2 = len(set(simulate(lines, 10)))
assert p1 == 6284
assert p2 == 2661
print(p1, p2, sep="\n")
