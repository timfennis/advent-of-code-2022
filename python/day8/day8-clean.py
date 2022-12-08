input = open('input').read()
lines = input.split('\n')

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row);
width, height = len(grid[0]), len(grid)

trees = set()
for y in range(0, height):
    current_best = -1
    for x in range(0, width):
        if grid[y][x] > current_best:
            trees.add((y, x))
            current_best = grid[y][x]
 
    current_best = -1
    for x in range(width - 1, -1, -1):
        if grid[y][x] > current_best:
            trees.add((y, x))
            current_best = grid[y][x] 

for x in range(0, width):
    current_best = -1
    for y in range(0, height):
        if grid[y][x] > current_best:
            trees.add((y, x))
            current_best = grid[y][x]
    current_best = -1
    for y in range(width - 1, -1, -1):
        if grid[y][x] > current_best:
            trees.add((y, x))
            current_best = grid[y][x]

p1 = len(trees)
print(p1)
assert p1 == 1763

def find_best_tree_score(ri: int, ci: int):
    up, down, left, right = 0, 0, 0, 0
    location_height = grid[ri][ci]
    x = ci
    for y in range(ri + 1, len(grid)):
        if grid[y][x] < location_height:
            down += 1
        if grid[y][x] >= location_height:
            down += 1
            break

    for y in range(ri - 1, -1, -1):
        if grid[y][x] < location_height:
            up += 1
        if grid[y][x] >= location_height:
            up += 1
            break

    y = ri
    for x in range(ci + 1, len(grid[0])):
        if grid[y][x] < location_height:
            right += 1
        if grid[y][x] >= location_height:
            right += 1
            break

    for x in range(ci - 1, -1, -1):
        if grid[y][x] < location_height:
            left += 1
        if grid[y][x] >= location_height:
            left += 1
            break

    return up * down * left * right

options = []
for y, row in enumerate(grid):
    for x, tree in enumerate(row):
       options.append(find_best_tree_score(y, x)) 

p2 = max(options)
print(p2)
assert p2 == 671160