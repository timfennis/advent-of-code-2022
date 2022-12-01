groups = open("input").read().split("\n\n")

totals = []
for group in groups:
    total = 0
    for line in group.split("\n"):
        total += int(line)
    
    totals.append(total)

print(sum(sorted(totals, reverse=True)[0:3]))