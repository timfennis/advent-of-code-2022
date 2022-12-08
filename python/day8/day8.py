input = open('input').read()
lines = input.split('\n')

grid = []
for line in lines:
    row = []
    for c in line:
        row.append(int(c))
    grid.append(row);


trees = set()
for row_idx, row in enumerate(grid):
    hight = -1
    print("LEFT TO RIGHT")
    for column_idx in range(0, len(row)):
        if grid[row_idx][column_idx] > hight:
            print("adding", (row_idx, column_idx))
            trees.add((row_idx, column_idx))
            hight = grid[row_idx][column_idx]

 
    hight = -1
    print("RIGHT TO LEFT")
    for column_idx in range(len(row) - 1, 0, -1):
        if grid[row_idx][column_idx] > hight:
            print("adding", (row_idx, column_idx), grid[row_idx][column_idx], hight)
            trees.add((row_idx, column_idx))
            hight = grid[row_idx][column_idx] 


for column_idx in range(0, len(grid[0])):
    hight = -1
    print("TOP TO BOTTOM")
    for row_idx in range(0, len(grid)):
        if grid[row_idx][column_idx] > hight:
            print("adding", (row_idx, column_idx), grid[row_idx][column_idx], hight)
            trees.add((row_idx, column_idx))
            hight = grid[row_idx][column_idx]
    hight = -1
    print("BOTTOM TO TOP")
    for row_idx in range(len(grid) - 1, 0, -1):
        if grid[row_idx][column_idx] > hight:
            print("adding", (row_idx, column_idx), grid[row_idx][column_idx], hight)
            trees.add((row_idx, column_idx))
            hight = grid[row_idx][column_idx]

print(len(trees))


def foo(ri: int, ci: int):
    print(f"---- considering {ri}, {ci} ----")
    tree_down = set()
    hight = grid[ri][ci]
    column_idx = ci
    for row_idx in range(ri + 1, len(grid)):
        if grid[row_idx][column_idx] < hight:
            tree_down.add((row_idx, column_idx))
        if grid[row_idx][column_idx] >= hight:
            tree_down.add((row_idx, column_idx))
            break

    print("TREE DOWN", tree_down)
    tree_up = set()
    hight = grid[ri][ci]
    for row_idx in range(ri - 1, -1, -1):
        if grid[row_idx][column_idx] < hight:
            tree_up.add((row_idx, column_idx))
        if grid[row_idx][column_idx] >= hight:
            tree_up.add((row_idx, column_idx))
            break
    print("TREES UP", tree_up)

    tree_right = set()
    hight = grid[ri][ci]
    row_idx = ri
    for column_idx in range(ci + 1, len(grid[0])):
        if grid[row_idx][column_idx] < hight:
            tree_right.add((row_idx, column_idx))
        if grid[row_idx][column_idx] >= hight:
            tree_right.add((row_idx, column_idx))
            break
    print("TREE RIGHT", tree_right)
    tree_left = set()
    hight = grid[ri][ci]
    for column_idx in range(ci - 1, -1, -1):
        if grid[row_idx][column_idx] < hight:
            tree_left.add((row_idx, column_idx))
        if grid[row_idx][column_idx] >= hight:
            tree_left.add((row_idx, column_idx))
            break
    print("TREE LEFT", tree_left)

    print("INTERMEDIATE ANSWER", len(tree_down), len(tree_up) , len(tree_left) , len(tree_right)) 
    return len(tree_down) * len(tree_up) * len(tree_left) * len(tree_right)

# print(foo(1, 2))
# print(foo(3, 2))

# exit()

options = []
for row_idx, row in enumerate(grid):
    for column_idx, tree in enumerate(row):
       options.append(foo(row_idx, column_idx)) 

print("FINAL ANSWER", max(options))