lines = [ line.strip() for line in open('input').read().split("\n") ]

cycle = 0
x = 1
samples = []
CRT = ['.' for _ in range(6 * 40)]

def update(cycle, x):
    if cycle > len(CRT):
        return
    if (cycle - 1) % 40 in [x - 1, x, x + 1]:
        CRT[cycle - 1] = '#'
    else:
        CRT[cycle - 1] = '.'

for line in lines:
    parts = line.split()
    cycle += 1
    update(cycle, x)
    samples.append((cycle, x))
    if len(parts) == 2:
        cycle += 1
        update(cycle, x)
        samples.append((cycle, x))
        x += int(parts[1])

print(sum([cycle * x for (cycle, x) in samples if (cycle + 20) % 40 == 0]))

for idx, char in enumerate(CRT):
    print(char, end="")
    if (idx + 1) % 40 == 0:
        print()
