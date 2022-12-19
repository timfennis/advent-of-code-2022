from collections import deque, defaultdict
from math import ceil
import sys
import functools

input = open('input' if len(sys.argv) < 2 else sys.argv[1]).read()

blueprints = dict()

for line in input.split('\n'):
    bp, rest = line.split(':')
    bp = int(bp.split(' ')[-1])
    costs = [it.strip() for it in rest.split('.')]
    ore_robot = int(costs[0].split('costs')[-1].strip(' ore '))
    clay_robot = int(costs[1].split('costs')[-1].strip(' ore' ))
    obsidian_robot = [int(it.strip(' ore ').strip(' clay ')) for it in costs[2].split('costs')[-1].strip().split(' and ')]
    geode_robot = [int(it.strip(' ore ').strip(' obsidian ')) for it in costs[3].split('costs')[-1].strip().split(' and ')]
    blueprints[bp] = [(-ore_robot, 0, 0 ,0), (-clay_robot, 0, 0, 0), (-obsidian_robot[0], -obsidian_robot[1], 0, 0), (-geode_robot[0], 0, -geode_robot[1], 0)]

def add(resource_count, robot_count):
    return tuple([ a + b for (a, b) in zip(resource_count, robot_count)])

def is_positive(b):
    return all([a >= 0 for a in b])

def strictly_better(a, b):
    return all([x >= y for x, y in zip(a, b)]) and \
        any([x > y for x, y in zip(a, b)])

def advance(resources, robots, minutes):
    r = resources
    for _ in range(minutes):
        r = add(r, robots)
    return r

def minutes_needed(resources, robots, target):
    time = 0
    r = resources
    while not is_positive(add(r, target)):
        r = add(r, robots)
        time += 1
        if time >= 30:
            return None

    return time

C = defaultdict(lambda: (0,0,0,0))

@functools.lru_cache(maxsize=None)
def sim_rec(costs, minutes, robot_count = (1,0,0,0), resource_count = (0,0,0,0)) -> int:
    if minutes == 0:
        return resource_count[3]

    current_best = C[minutes, robot_count]

    # Throw away excess resources
    mx = (
        max([abs(x) for x, _, _, _ in costs]),
        max([abs(x) for _, x, _, _ in costs]),
        max([abs(x) for _, _, x, _ in costs]),
        0
    )

    resource_count = (
        min(mx[0] * 2, resource_count[0]),
        min(mx[1] * 2, resource_count[1]),
        min(mx[2] * 2, resource_count[2]),
        resource_count[3]
    )

    # Fooo
    if strictly_better(resource_count, current_best):
        C[minutes, robot_count] = resource_count
    elif strictly_better(current_best, resource_count):
        return 0 # FUCK IT THIS SOLUTION SUCKS ASSSSSSSSSSSSSS

    # Find the best option
    best, possibilities_remaining = 0, False
    # Buy ore bot
    for cost, effect in zip(list(costs), [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]):
        # Calc minutes needed
        mn = minutes_needed(resource_count, robot_count, cost)

        # Never buy more than 4 ore bots
        if robot_count[0] >= mx[0] and effect == (1,0,0,0): continue
        if robot_count[1] >= mx[1] and effect == (0,1,0,0): continue
        if robot_count[2] >= mx[2] and effect == (0,0,1,0): continue
        
        if mn is not None and minutes - (mn + 1) >= 0:
            # Increment the time until we can afford the new robot (and one extra time to skip ahead to the end of the minute)
            new_resources = advance(resource_count, robot_count, mn)
            # Remove the cost of the robot from our new resources
            new_resources = add(new_resources, cost)
            # Buy the new robot
            new_bot_count = add(robot_count, effect)
            
            # Add an extra minute worth of resources
            new_resources = add(new_resources, robot_count)

            # Take an extra minute worth of time
            best = max(best, sim_rec(costs, minutes - (mn + 1), new_bot_count, new_resources))
            possibilities_remaining = True
    
    if not possibilities_remaining:
        # We must simulate till the end
        return (minutes * robot_count[3]) + resource_count[3]
    return best

score = 0
for idx, costs in blueprints.items():
    sub = sim_rec(tuple(costs), 24)
    C.clear()
    sim_rec.cache_clear()
    score += idx * sub

print("Part 1", score)
score = 1
for idx, costs in blueprints.items():
    if idx >= 4:
        break
    sub = sim_rec(tuple(costs), 32)
    C.clear()
    sim_rec.cache_clear()
    score *= sub

# Expected for example is 56 and 62
print("Part 2", score)  