lines = [ line.strip() for line in open('input').read().split("\n") ]

cycle, x = 0, 1
samples = []
CRT = ['.' for _ in range(6 * 40)]

def update(cycle, x):
    cycle += 1
    samples.append((cycle, x))
    if (cycle - 1) % 40 in [x - 1, x, x + 1]:
        CRT[cycle - 1] = '#'

for line in lines:
    update(cycle, x)
    if line.startswith('addx'):
        update(cycle, x)
        x += int(line.split()[-1])

print(sum([cycle * x for (cycle, x) in samples if (cycle + 20) % 40 == 0]))

for idx, char in enumerate(CRT):
    print(char, end="")
    if (idx + 1) % 40 == 0:
        print()
