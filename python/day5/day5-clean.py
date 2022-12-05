from copy import deepcopy
import re

input = open('input').read()
config, input = input.split('\n\n')
stacks = [list('') for _ in range(0, 9)]

for l in config.split('\n'):
    for idx, c in enumerate(l[1::4]):
        if c.isalnum():
            stacks[idx].insert(0, c)

def part1(stacks: list[str], fr: int, to: int, cnt: int):
    stacks[to] = stacks[to] + stacks[fr][-cnt:][::-1]
    stacks[fr] = stacks[fr][:-cnt] 
    return stacks

def part2(stacks: list[str], fr: int, to: int, cnt: int):
    stacks[to] = stacks[to] + stacks[fr][-cnt:]
    stacks[fr] = stacks[fr][:-cnt] 
    return stacks

p1 = deepcopy(stacks)
p2 = deepcopy(stacks)

for line in input.split('\n'):
    cn, fr, to = [int(it) for it in re.findall(r"(\d+)", line)]
    p1 = part1(p1, fr - 1, to - 1, cn)
    p2 = part2(p2, fr - 1, to - 1, cn)

p1a = ''.join([stack[-1] for stack in p1])
assert p1a == 'CVCWCRTVQ'
print(p1a)
p2a = ''.join([stack[-1] for stack in p2])
assert p2a == 'CNSCZWLVT'
print(p2a)