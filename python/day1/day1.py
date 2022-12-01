groups = open("input").read().split("\n\n")

totals = [sum([int(x) for x in group.split("\n")]) for group in groups].sort(reverse=True)

print(totals[0])
print(sum(totals[0:3]))