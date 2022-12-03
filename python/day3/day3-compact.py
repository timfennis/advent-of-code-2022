import string
from functools import reduce

lines = open("input").read().split("\n")
alpha = "_" + string.ascii_lowercase + string.ascii_uppercase

def solve(groups: list):
    match = reduce(lambda a, b: a & b, [set(x) for x in groups], set(alpha))
    return alpha.index(*match)
    
print(sum([solve([line[len(line) // 2:], line[:len(line) // 2]]) for line in lines]))
print(sum([solve(lines[x:x+3]) for x in range(0, len(lines), 3)]))