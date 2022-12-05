input = open('input').read()

#     [P]                 [C] [C]    
#     [W]         [B]     [G] [V] [V]
#     [V]         [T] [Z] [J] [T] [S]
#     [D] [L]     [Q] [F] [Z] [W] [R]
#     [C] [N] [R] [H] [L] [Q] [F] [G]
# [F] [M] [Z] [H] [G] [W] [L] [R] [H]
# [R] [H] [M] [C] [P] [C] [V] [N] [W]
# [W] [T] [P] [J] [C] [G] [W] [P] [J]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    list('WRF'),
    list('THMCDVWP'),
    list('PMZNL'),
    list('JCHR'),
    list('CPGHQTB'),
    list('GCWLFZ'),
    list('WVLQZJGC'),
    list('PNRFWTVC'),
    list('JWHGRSV'),
]

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

p1 = stacks.copy()
p2 = stacks.copy()

for line in input.split('\n'):
    a, to = line.split(' to ')
    b, fr = a.split(' from ')
    _, cn = b.split('e ')
    to, fr, cn = int(to) - 1, int(fr) - 1, int(cn)

    p1 = part1(p1, fr, to, cn)
    p2 = part2(p2, fr, to, cn)

print(''.join([stack[-1] for stack in p1]))
print(''.join([stack[-1] for stack in p2]))