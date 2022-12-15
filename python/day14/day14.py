from collections import defaultdict
from copy import deepcopy
import sys

do_print = True if '--print' in sys.argv else False
file_arg = [arg for arg in sys.argv[1:] if arg != '--print']
input = open(file_arg[0] if len(file_arg) >= 1 else 'input').read()
lines = input.split('\n')

grid = defaultdict(lambda: '.')

for line in lines:
    path = [(int(x), int(y)) for x, y in [pair.split(',') for pair in line.split(' -> ')]]

    for (sx, sy), (ex, ey) in list(zip(path, path[1:])):
        sx, ex = sorted([sx, ex])
        sy, ey = sorted([sy, ey])
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                grid[(x,y)] = '#'

def get_bounds(grid: defaultdict[tuple[int, int], str]):
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

def find_move(grid: defaultdict[tuple[int, int], str], sand: tuple[int, int], maxy: int):
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
def run_simulation(input_grid: defaultdict[tuple[int, int], str], part1: bool):
    grid = deepcopy(input_grid)
    _, _, _, maxy = get_bounds(grid)
    sand_origin = (500, 0)
    continue_simulation = True
    while continue_simulation:
        # Spawn 1 below the origin
        sand = (sand_origin[0], sand_origin[1])
        while True:
            move = find_move(grid, sand, None if part1 else maxy + 2)

            if move == None:
                grid[sand] = 'o'
                if part1 == False and sand == sand_origin:
                    continue_simulation = False
                break
            else:
                if part1 and sand[1] > maxy:
                    continue_simulation = False
                    break
                sand = move
    
    return grid

# Print initial grid state
do_print and print_state(grid)

# Print part 1
p1_grid = run_simulation(grid, True)
do_print and print_state(p1_grid)
print(sum(1 for x in p1_grid.values() if x == 'o'))

# Print part 2
p2_grid = run_simulation(grid, False)
do_print and print_state(p2_grid)
print(sum(1 for x in p2_grid.values() if x == 'o'))