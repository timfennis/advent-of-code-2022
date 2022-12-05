from copy import deepcopy

input = open('input').read()
config, input = input.split('\n\n')
stacks = [list('') for _ in range(0, 9)]

for l in config.split('\n'):
    for idx, c in enumerate(l):
        if c.isalnum():
            stacks[(idx - 1) // 4].insert(0, c)

def part1(stacks: list[str], fr: int, to: int, cnt: int):
    move = stacks[fr][-cnt:]
    stacks[fr] = stacks[fr][:-cnt]
    
    stacks[to] = stacks[to] + move[::-1]
    return stacks

def part2(stacks: list[str], fr: int, to: int, cnt: int):
    move = stacks[fr][-cnt:]
    stacks[fr] = stacks[fr][:-cnt]
    
    stacks[to] = stacks[to] + move
    return stacks

p1 = deepcopy(stacks)
p2 = deepcopy(stacks)

for line in input.split('\n'):
    a, to = line.split(' to ')
    b, fr = a.split(' from ')
    _, cn = b.split('e ')
    to, fr, cn = int(to) - 1, int(fr) - 1, int(cn)

    p1 = part1(p1, fr, to, cn)
    p2 = part2(p2, fr, to, cn)

print(''.join([stack[-1] for stack in p1]))
print(''.join([stack[-1] for stack in p2]))