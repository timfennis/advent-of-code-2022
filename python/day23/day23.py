from collections import deque
data = open('input').read()

def print_grid():
    for y in range(min_x -1, max_y+2):
        for x in range(min_y - 1, max_x+2):
            print('#' if (y,x) in elves.keys() else '.', end='')
        print()

elves = dict()

for row, line in enumerate(data.split('\n')):
    for col, char in enumerate(line):
        if char == '#':
            elves[row, col] = False

dirs8 = [(-1,-1), (-1,0), (-1,1),
         (0,-1), (0,1), #center is banned
         (1,-1), (1,0), (1,1)]

dirs4 = deque([
    [(-1,-1),(-1,0),(-1,1)],
    [(1,-1),(1,0),(1,1)],
    [(1,-1),(0,-1),(-1,-1)],
    [(1,1),(0,1),(-1,1)]
])

num = 0
while True:
    for ((cr, cc), _) in elves.items():
        all_clear = True
        for dr, dc in dirs8:
            nr, nc =  cr + dr, cc + dc
            if (nr, nc) in elves.keys():
                all_clear = False
                break

        if not all_clear:
            for dirs in dirs4:
                hit = False
                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if (nr, nc) in elves.keys():
                        hit = True
                        break
                if not hit:
                    dr, dc = dirs[1] # middle value is the dir
                    nr, nc = cr + dr, cc + dc
                    elves[cr, cc] = (nr, nc)
                    break
    # Do the dance
    new_elves = dict()
    move_list = list(elves.values())
    for (cur_pos, move) in elves.items():
        if isinstance(move, tuple):
            if move_list.count(move) == 1:
                # move
                new_elves[move] = False
            else: 
                # skip move
                new_elves[cur_pos] = False
                pass
        else:
            # If we aren't allowed to move just stand here
            new_elves[cur_pos] = False

    assert len(new_elves) != 0

    num += 1
    if new_elves == elves:
        print("part 2", num)
        elves = new_elves

        break
    else:
        elves = new_elves

    if num == 10:
        min_x = min(x for y, x in elves.keys())
        max_x = max(x for y, x in elves.keys())
        min_y = min(y for y, x in elves.keys())
        max_y = max(y for y, x in elves.keys())

        print("part 1", (((max_x - min_x) + 1) * ((max_y - min_y) + 1)) - len(elves.keys()))

    # shift dirs 4 
    head = dirs4.popleft()
    dirs4.append(head)
    
        