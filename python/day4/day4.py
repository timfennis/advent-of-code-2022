input = open("input").read()

full = 0
partial = 0
for line in input.split():
    a, b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')

    r1 = set(range(int(a1), int(a2) + 1))
    r2 = set(range(int(b1), int(b2) + 1))

    r3 = r1 & r2

    if r1 == r3 or r2 == r3:
        full += 1

    if len(r3) > 0:
        partial += 1

print(full)
print(partial)