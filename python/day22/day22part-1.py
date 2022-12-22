from collections import defaultdict
from copy import deepcopy
import sys

data = open('example').read()
data = open('input').read()

grid, instructions = data.split('\n\n')

G = defaultdict(lambda: None)
for row, line in enumerate(grid.split('\n')):
    for col, char in enumerate(list(line)):
        if char in ['.', '#']:
            G[(row, col)] = char

ins = []
acc = ''
for c in instructions:
    if c in ['L', 'R']:
        ins.append(int(acc))
        acc = ''
        ins.append(c)
    else:
        acc += c

ins.append(int(acc))

# print(ins)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs2 = ['>', 'v', '<', '^']

def turn(current_direction, modifier):
    idx = dirs.index(current_direction)
    if modifier == 'L':
       return dirs[(idx - 1) % len(dirs)]
    elif modifier == 'R':
       return dirs[(idx + 1) % len(dirs)]
    else:
        assert False

# print(turn((0,1), 'R'))
# print(turn(turn((0,1), 'R'), 'R'))
# print(turn(turn(turn((0,1), 'R'), 'R'), 'R'))
# print(turn(turn(turn(turn((0,1), 'R'), 'R'), 'R'), 'R'))
# print(turn(turn(turn(turn(turn((0,1), 'R'), 'R'), 'R'), 'R'), 'R'))

def print_grid(grid):
    min_r = min(row for row, col in grid.keys())
    max_r = max(row for row, col in grid.keys())
    min_c = min(col for row, col in grid.keys())
    max_c = max(col for row, col in grid.keys())
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            print(grid[r, c] if grid[r, c] is not None else ' ', end='')
        print()

cur_pos = (0, min([col for ((row, col), _) in G.items() if row == 0]))
facing = (0, 1)

DG = deepcopy(G)
for ins_idx, instr in enumerate(ins):
    # if len(sys.argv) >= 2 and ins_idx >= int(sys.argv[1]):
    #     print_grid(DG)
    #     break
    
    # print_grid(DG)
    # input()
    # print("executing", instr)
    if instr in ['L', 'R']:
        facing = turn(facing, instr)
        DG[cur_pos] = dirs2[dirs.index(facing)]
    else:
        for _ in range(instr):
            nr, nc = cur_pos[0] + facing[0], cur_pos[1] + facing[1]
            obj = G[nr, nc]

            if obj == '.':
                cur_pos = (nr, nc)
                DG[cur_pos] = dirs2[dirs.index(facing)]
            elif obj == '#':
                break
            elif obj is None:
                dr, dc = facing
                if dr == -1: # We're moving up, out of the top of the map
                    #new pos is the bottom slot for this column
                    nr = max([row for row, col in G.keys() if col == cur_pos[1] and G[row, col] != None])
                elif dr == 1: # We're moving down
                    nr = min([row for row, col in G.keys() if col == cur_pos[1] and G[row, col] != None])
                elif dc == -1: # We're moving left
                    nc = max([col for row, col in G.keys() if row == cur_pos[0] and G[row, col] != None])
                elif  dc == 1: # We're moving right
                    nc= min([col for row, col in G.keys() if row == cur_pos[0] and G[row, col] != None])
                else:
                    assert False

                obj = G[nr, nc]

                if obj == '.':
                    cur_pos = (nr, nc)
                    DG[cur_pos] = dirs2[dirs.index(facing)]
                elif obj == '#':
                    break
                elif obj is None:
                    print("Invalid state 1234")
                    assert False
            else:
                print("Invalid state foooo")
                assert False


a, b = cur_pos
c = dirs.index(facing)
print((1000 * (a + 1)) + (4 * ((b+1)) + c))
