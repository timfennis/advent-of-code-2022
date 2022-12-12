from collections import defaultdict

input = open('input').read()
grid = [list(it) for it in input.split('\n')]

WIDTH = len(grid[0])
HEIGHT = len(grid)

sx, sy = 0, 0
ex, ey = 0, 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'S':
            sx, sy = x, y
        if char == 'E':
            ex, ey = x, y

grid[sy][sx] = 'a'
grid[ey][ex] = 'z'

def find_shortest_path(sx, sy, reverse = False):
    paths = defaultdict(lambda: 10e15)
    paths[(sy, sx)] = 0
    should_search = [(sx, sy, 0)]
    while len(should_search) > 0:
        x, y, steps = should_search[0]
        should_search = should_search[1:]
        from_height = ord(grid[y][x])

        for (dx, dy) in directions:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
                continue
                
            to_height = ord(grid[ny][nx])
            
            # If we're searching for a path up we can move down as much as we want, but only up by 1 level at a time
            if not reverse and not from_height - to_height >= -1:
                continue
            
            # If we're searching in reverse we can only go down one level but up as much as we want
            if reverse and not from_height - to_height <= 1:
                continue

            if paths[(ny, nx)] > steps + 1:
                paths[(ny, nx)] = steps + 1
                should_search.append((nx, ny, steps + 1))
    return paths

part1 = find_shortest_path(sx, sy)[ey, ex]
print(part1)

part2 = min([dist for ((y, x), dist) in find_shortest_path(ex, ey, True).items() if grid[y][x] == 'a'])
print(part2)