instructions = open('input').read()
# instructions = open('example').read()
total_different_instructions = sum([1 for x in instructions if x in ['>', '<']])


rocks = [
    # RRRR
    [(0,0), (1,0), (2,0), (3,0)],
    #  R
    # RRR
    #  R
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    # ..R
    # ..R
    # RRR
    [(2,0), (2,1), (0,2), (1,2), (2,2)],
    # R
    # R
    # R
    # R
    [(0,0), (0,1), (0,2), (0,3)],
    # RR
    # RR
    [(0,0), (0,1), (1,0), (1,1)],
]

directions = {
    'left': (-1, 0),
    'right': (1, 0),
    'down': (0, 1), # Down is an increase in y
}

def collides_with_tower(tower, object, move):
    dx, dy = move
    for x, y in object:
        nx, ny = x + dx, y + dy
        if (nx, ny) in tower or ny >= 1:
            return True
    return False
def get_tower_height(tower):
    min_y = min([y for _, y in tower] + [1])
    max_y = max([y for _, y in tower] + [1])

    return max_y - min_y

def print_tower_rev(tower):
    min_y = min([y for _, y in tower] + [0]) - 2
    max_y = max([y for _, y in tower] + [0]) + 2
    for y in range(max_y, min_y, - 1):
        for x in range(7):
            if (x,y) in tower:
                print('#', end='')
            elif y == 1:
                print('X', end='')
            else:
                print('.', end='')
        print()
def print_tower(tower):
    min_y = min([y for _, y in tower] + [0])
    max_y = max([y for _, y in tower] + [0]) + 2
    for y in range(min_y, max_y):
        for x in range(7):
            if (x,y) in tower:
                print('#', end='')
            elif y == 1:
                print('X', end='')
            else:
                print('.', end='')
        print()

def move(object, direction, max_width = 7):
    dx, dy = direction

    if dx > 0:
        max_x = max([x for x, _ in object]) + dx
        if max_x not in range(0, max_width):
            return object
    elif dx < 0:
        min_x = min([x for x, _ in object]) + dx
        if min_x not in range(0, max_width):
            return object 
    return [(x + dx, y + dy) for (x, y) in object]

def sim_tower(h: int):
    tower = set()
    rock_idx = 0
    jet_idx = 0
    for i in range(h):
        rock = rocks[rock_idx % len(rocks)]

        current_tower_height = get_tower_height(tower)
        
        rock_height = max([y for _, y in rock]) + 1
        rock = move(rock, (2, 0 - (current_tower_height + rock_height + 2)))
        
        rock_idx += 1
        collide = False
        
        while collide == False: # No collission
            instruction = instructions[jet_idx]
            if instruction == '>':
                direction = directions['right']
            elif instruction == '<':
                direction = directions['left']
            else: raise ValueError(f'Unexpected instruction {instruction}')


            cannot_move = collides_with_tower(tower, rock, direction)
            if not cannot_move:
                rock = move(rock, direction)
            jet_idx += 1
            jet_idx %= len(instructions)

            # Check if downward movement is possible

            collide = collides_with_tower(tower, rock, directions['down'])
            if collide == False:
                rock = move(rock, directions['down'])
                # print('-- moving down --')

                # print_tower(tower | set(rock))
            else:
                tower |= set(rock)

    return (tower, get_tower_height(tower))
        # if get_tower_height(tower) == 2767:
        #     print(rock_idx - 97)
        #     exit()

_, h1 = sim_tower(97 + 1715)
_, h2 = sim_tower(97 + 1715 + 1633)
# print_tower_rev(tower)

# print("height", get_tower_height(tower))

# pad_rocks = 15
# pad_height = 25
# rock_inc = 35
# height_inc = 53

######
desired_rock_sim = 1000000000000
pad_rocks = 97
pad_height = 151
rock_inc = 1715
height_inc = 2616

rock_sim = (desired_rock_sim-pad_rocks)
print("Simulations needed after padding is removed", rock_sim)
mod = rock_sim % rock_inc
div = rock_sim // rock_inc
height = div * height_inc
print("Simulations remaining afterwards", mod)

print(height + pad_height)
print(height + pad_height + (h2 - h1)) # NOT EVEN SURE WHY THIS IS CORRECT
# print(1514285714288)

# 1525364431490 too high