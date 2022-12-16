import re
import sys
import functools
from itertools import combinations, permutations
from copy import copy

input = open(sys.argv[1] if len(sys.argv) >= 2 else 'example').read()

FLOW_RATES = dict()
NETWORK = dict()

for line in input.split('\n'):
    pipe, rate, connections = re.findall(r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)[0]
    rate = int(rate)
    NETWORK[pipe] = connections.split(', ')
    FLOW_RATES[pipe] = rate

FINAL_RATE = sum(FLOW_RATES.values())

def distance(s: str, d: str, path = set()) -> int:
    if s == d:
        return 0

    paths = []
    for node in [x for x in NETWORK[s] if x not in path]:
        visited = copy(path)
        visited.add(node)
        foo = distance(node, d, visited) 
        if foo != None:
            paths.append(1 + foo)

    if len(paths) == 0:
        return None 

    return min(paths)
    
DISTANCE_TABLE = dict() 
USEFULL_NODES = [node for (node, rate) in FLOW_RATES.items() if rate > 0]
USEFULL_NODES.append('AA')

for a, b in list(combinations(USEFULL_NODES, 2)):
    DISTANCE_TABLE[(a, b)] = distance(a, b, set(a))
    DISTANCE_TABLE[(b, a)] = distance(b, a, set(b))

USEFULL_NODES.remove('AA')

@functools.lru_cache(maxsize=None)
def solve(our_loc: str, ele_loc: str, our_time: int, ele_time: int, opened_valves: frozenset[str]) -> int:

    rate = sum([FLOW_RATES[node] for node in opened_valves])

    # if our_time == 26 and ele_time == 26:
        # return 0

    # Look for other options
    destinations = [node for node in USEFULL_NODES if node not in opened_valves]

    # 
    options = []
    for our_next_loc in destinations:
        for ele_next_loc in destinations:
            # We dont' want to go to the same location
            if our_next_loc == ele_next_loc:
                continue
     
            our_cost, ele_cost = 1, 1

            valves_opened_now = []
            if our_next_loc == our_loc:
                valves_opened_now.append(our_loc)
            else:
                our_cost = DISTANCE_TABLE[(our_loc, our_next_loc)]
                # Skip options that are too expensive
                if our_time + our_cost > 26:
                    continue
            # If we stay, open valve
            if ele_next_loc == ele_loc:
                valves_opened_now.append(ele_loc)
            else:
                ele_cost = DISTANCE_TABLE[(ele_loc, ele_next_loc)]
                # Skip options that are too expensive
                if ele_time + ele_cost > 26:
                    continue

            solution = rate + solve(our_next_loc, ele_next_loc,
                our_time + our_cost, ele_time + ele_cost,
                opened_valves.union(frozenset(valves_opened_now))
            )
            options.append(solution)
    
    if len(options) == 0:
        return rate

    # Return the best option
    return max(options)

# solution = solve('AA', 'AA', 0, 0, frozenset())
# print(solution)

def possible_paths(start, budget, exclude = None):
    if exclude == None: exclude = set()
    if budget >= 1:
        yield [start]
    for n in USEFULL_NODES:
        if start == n: continue
        if n in exclude: continue
        cost = DISTANCE_TABLE[start, n]
        if budget >= cost + 2:
            for path in possible_paths(n, budget - cost - 1, exclude | set([start])):
                yield [start] + path
    
@functools.cache
def path_value(path, budget) -> int:
    value = 0
    for cur, next in zip(path[0:], path[1:]):
        budget -= DISTANCE_TABLE[cur, next] 
        node_rate = FLOW_RATES[next]
        if node_rate > 0:
            budget -= 1
            value += node_rate * budget
        
    return value

best = 0
for pp in possible_paths('AA', 30):
    best = max(best, path_value(tuple(pp), 30))

print(best)

best = 0
count = 0
for p1 in possible_paths('AA', 26):
    print(count)
    for p2 in possible_paths('AA', 26, exclude=set(p1)):
        best = max(best, path_value(tuple(p1), 26) + path_value(tuple(p2), 26))
    count += 1
print(best)