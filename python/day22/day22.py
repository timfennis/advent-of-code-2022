from collections import defaultdict

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR_MAP = {
    'right': DIRS[0],
    'down': DIRS[1],
    'left': DIRS[2],
    'up': DIRS[3],
}

flip_axis = lambda n: 51 - n

def turn(current_direction, modifier):
    idx = DIRS.index(current_direction)
    return DIRS[(idx + 1 if modifier == 'R' else idx - 1) % len(DIRS)]

def wrap_p1(nr, nc, nd):
    dr, dc = nd
    if dr == -1: # We're moving up, out of the top of the map
        #new pos is the bottom slot for this column
        nr = max([row for row, col in G.keys() if col == nc and G[row, col] != None])
    elif dr == 1: # We're moving down
        nr = min([row for row, col in G.keys() if col == nc and G[row, col] != None])
    elif dc == -1: # We're moving left
        nc = max([col for row, col in G.keys() if row == nr and G[row, col] != None])
    elif  dc == 1: # We're moving right
        nc= min([col for row, col in G.keys() if row == nr and G[row, col] != None])
    else:
        raise ValueError('Invalid OOB case')
    return nr, nc, nd

def wrap_p2(nr, nc, nd):
    # Exiting to the top of 1 (entering left of 6)
    if nr == 0 and nc in range(51, 100 + 1):
        nr = 150 + (nc - 50)
        nc = 1 #lhs
        nd = DIR_MAP['right']
    # Exiting to the left of 6 entering the top of 1
    elif nc == 0 and nr in range(151, 200 + 1):
        nc = 50 + (nr - 150)
        nr = 1 #top
        nd = DIR_MAP['down']
    # Exiting to the left of 1 (entering the left of 5)
    elif nc == 50 and nr in range(1, 50 + 1):
        nr = 100 + flip_axis(nr)
        nc = 1 #lhs
        nd = DIR_MAP['right']
    # Exiting to the left of 5 (entering left of 1)
    elif nc == 0 and nr in range(101, 150 + 1):
        nr = flip_axis(nr - 100)
        nc = 51 #lhs
        nd = DIR_MAP['right']
    # Exiting at the top of 2 (entering bottom of 6)
    elif nr == 0 and nc in range(101, 150 + 1):
        nc = (nc - 100)
        nr = 200 # bottom
        nd = DIR_MAP['up'] # facing stays the same but has to be rewritten
    # Exiting the bottom of 6 (entering the top of 2)
    elif nr == 201 and nc in range(1, 50 + 1):
        nc = nc + 100
        nr = 1 # top
        nd = DIR_MAP['down'] # facing stays the same but has to be rewritten
    # Exiting the right of 2 (entering the right of 4)
    elif nc == 151 and nr in range(1, 50 + 1):
        nr = flip_axis(nr) + 100
        nc = 100 # rhs
        nd = DIR_MAP['left']
    # Exiting the right of 4 (entering the right of 2)
    elif nc == 101 and nr in range(101, 150 + 1):
        nr = flip_axis(nr - 100)
        nc = 150 # rhs
        nd = DIR_MAP['left']
    # Exiting the bottom of 4 (entering the right of 6)
    elif nr == 151 and nc in range(51, 100 + 1) and nd == DIR_MAP['down']:
        nr = 150 + (nc - 50) # Mapping 51..=100 to 151..=200
        nc = 50 # rhs
        nd = DIR_MAP['left']
    # Exiting the right of 6 (entering bottom of 4)
    elif nc == 51 and nr in range(151, 200 + 1) and nd == DIR_MAP['right']:
        nc = (nr - 150) + 50
        nr = 150 # bottom
        nd = DIR_MAP['up']
    # Exiting the bottom of 2 (entering right of 3)
    elif nr == 51 and nc in range(101, 150 + 1) and nd == DIR_MAP['down']:
        nr = (nc - 100) + 50
        nc = 100 # rhs of 3
        nd = DIR_MAP['left']
    # right of 3 to bottom of 2
    elif nc == 101 and nr in range(51, 100 + 1) and nd == DIR_MAP['right']:
        nc = (nr - 50) + 100
        nr = 50 # bottom
        nd = DIR_MAP['up']
    # Exiting the left of 3 to top of 5
    elif nc == 50 and nr in range(51, 100 + 1) and nd == DIR_MAP['left']:
        # print(nc, nr, facing)
        nc = (nr - 50)
        nr = 101 #top
        nd = DIR_MAP['down']
    # exiting top of 5, entering left of 3
    elif nr == 100 and nc in range(1, 50 + 1) and nd == DIR_MAP['up']:
        nr = nc + 50
        nc = 51
        nd = DIR_MAP['right']
    else:
        raise ValueError("Unexpected OOB case")
    return nr, nc, nd

def score(cur_pos, dir):
    return sum([1000 * cur_pos[0], 4 * cur_pos[1], DIRS.index(dir)])

def run_simulation(instructions, wrapping_func):
    cur_pos = (1, min([col for ((row, col), _) in G.items() if row == 1]))
    facing = (0, 1)

    for ins in instructions:
        if ins in ['L', 'R']:
            facing = turn(facing, ins)
        else:
            for _ in range(ins):
                nr, nc, nf = cur_pos[0] + facing[0], cur_pos[1] + facing[1], facing

                # Fix OOB 
                if G[nr, nc] is None:
                    nr, nc, nf = wrapping_func(nr, nc, facing)
                
                if G[nr, nc] == '.':
                    cur_pos = (nr, nc)
                    facing = nf
                elif G[nr, nc] == '#':
                    break
    return cur_pos, facing

data = open('input').read()

grid, inst_data = data.split('\n\n')

G = defaultdict(lambda: None)
for row, line in enumerate(grid.split('\n')):
    for col, char in enumerate(list(line)):
        if char in ['.', '#']:
            G[(row + 1, col + 1)] = char

inst, acc = [], ''
for c in inst_data:
    if c in ['L', 'R']:
        inst.append(int(acc))
        acc = ''
        inst.append(c)
    else:
        acc += c
inst.append(int(acc))

print(score(*run_simulation(inst, wrap_p1)))
print(score(*run_simulation(inst, wrap_p2)))
