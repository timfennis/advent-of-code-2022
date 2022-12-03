import string
input = open('input').read()


total = 0
for line in input.split('\n'):
    l = int(len(line) / 2)

    F = set(line[:l])
    S = set(line[l:])
    
    for d in F.intersection(S):
        if d in string.ascii_uppercase:
            num = string.ascii_uppercase.index(d) + 27
        elif d in string.ascii_lowercase:
            num = string.ascii_lowercase.index(d) + 1

        total += num


print(total)

lines = input.split('\n');

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

total = 0

for group in groups:

    A = set(group[0])
    B = set(group[1])
    C = set(group[2])
    
    for d in A.intersection(B, C):
        if d in string.ascii_uppercase:
            num = string.ascii_uppercase.index(d) + 27
        elif d in string.ascii_lowercase:
            num = string.ascii_lowercase.index(d) + 1

        total += num


print(total)
