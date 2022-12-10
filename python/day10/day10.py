input = open('input').read()
lines = [ line.strip() for line in input.split("\n") ]

cycle = 0
x = 1
samples = []
line_nr = 0
CRT = ['.' for _ in range(6 * 40)]

def update(cycle, x):
    a, b, c = x - 1, x, x + 1
    if cycle >= len(CRT):
        return
    if cycle % 40 in [a,b,c]:
        CRT[cycle] = '#'
    else:
        CRT[cycle] = '.'
for line in lines:
    update(cycle, x)
    cycle += 1
    line_nr += 1
    parts = line.split()
    if len(parts) == 1:
        if (cycle + 20) % 40 == 0:
            samples.append((cycle, x, line_nr))
    elif len(parts) == 2:
        if (cycle + 20) % 40 == 0:
            samples.append((cycle, x, line_nr))
        update(cycle, x)
        cycle += 1
        if (cycle + 20) % 40 == 0:
            samples.append((cycle, x, line_nr))
        
        x += int(parts[1])

print(samples)
for idx, char in enumerate(CRT):
    if idx % 40 == 0:
        print()
    else:
        print(char, end="")

print(sum([a * b for a, b, _ in samples]))


