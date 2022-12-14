from collections import defaultdict
from copy import deepcopy

input = open('input').read()
lines = input.split('\n')

grid = defaultdict(lambda: '.')

for line in lines:
    path = []
    for coord in line.split(' -> '):
        x, y = coord.split(',')
        path.append((int(x), int(y)))

    zipped = list(zip(path, path[1:]))
    for (sx, sy), (ex, ey) in zipped:
        stepx = -1 if sx > ex else 1 
        stepy = -1 if sy > ey else 1
        for y in range(sy, ey + stepy, stepy):
            for x in range(sx, ex + stepx, stepx):
                grid[(x,y)] = '#'

def get_bounds(grid):
    min_x, max_x, min_y, max_y = 999999999, 0, 999999999, 0
    for (x,y), _ in grid.items():
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    return min_x, max_x, min_y, max_y

def print_state(grid):
    minx, maxx, miny, maxy = get_bounds(grid)
    G = [[grid[(x,y)] for x in range(minx, maxx + 1)] for y in range(miny, maxy + 1)]
    for row in G:
        print("".join(row))

def find_move(grid, sand, maxy):
    down = lambda p: (p[0], p[1]+1)
    diag_left = lambda p: (p[0]-1, p[1]+1)
    diag_right = lambda p: (p[0]+1, p[1]+1)

    for op in [down, diag_left, diag_right]:
        nx, ny = op(sand)

        if maxy != None and ny == maxy:
            return None
        # If we can move the sand in the current direction let's do it
        if grid[(nx, ny)] == '.':
            return (nx, ny)
    return None


# Simulation time
def run_simulation(input_grid, part1):
    grid = deepcopy(input_grid)
    _, _, _, maxy = get_bounds(grid)
    sand_origin = (500, 0)
    continue_simulation = True
    moves = 0
    while continue_simulation:
    # for _ in range(24):
        # Spawn 1 below the origin
        sand = (sand_origin[0], sand_origin[1])
        while True:
            move = find_move(grid, sand, None if part1 else maxy + 2)

            if move == None:
                moves += 1
                grid[sand] = 'o'
                if part1 == False and sand == sand_origin:
                    continue_simulation = False
                break
            else:
                if part1 and sand[1] > maxy:
                    continue_simulation = False
                    break
                sand = move
    
    return (moves, grid)

# Print initial grid state
print_state(grid)

p1_moves, p1_grid = run_simulation(grid, True)
print_state(p1_grid)
print(p1_moves)

p2_moves, p2_grid = run_simulation(grid, False)
print(p2_moves)
print_state(p2_grid)