import re
import sys
import functools
from copy import copy
from itertools import combinations

input = open(sys.argv[1] if len(sys.argv) >= 2 else 'input').read()

FLOW_RATES = dict()
NETWORK = dict()

for line in input.split('\n'):
    pipe, rate, connections = re.findall(r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)[0]
    rate = int(rate)
    NETWORK[pipe] = connections.split(', ')
    FLOW_RATES[pipe] = rate


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
def solve(current_node, time_remaining, enabled_nodes = None, players_remaining = 0):
    if enabled_nodes is None: enabled_nodes = frozenset() 

    if time_remaining == 0:
        if players_remaining > 0:
            return solve('AA', 26 - 1, enabled_nodes, players_remaining - 1)
        else:
            return 0

    best = 0
    if current_node not in enabled_nodes and FLOW_RATES[current_node] > 0:
        new_total = time_remaining * FLOW_RATES[current_node]
        best = new_total + solve(current_node, time_remaining-1, enabled_nodes | frozenset([current_node]), players_remaining) 

    # Look for other options
    for next_node in [node for node in USEFULL_NODES]:
        if next_node in enabled_nodes: continue
        if next_node == current_node: continue

        cost = DISTANCE_TABLE[current_node, next_node]

        if time_remaining - cost < 0: continue
        best = max(best, solve(next_node, time_remaining-cost, enabled_nodes, players_remaining))
    
    return best

print(solve('AA', 30 - 1, None, 0))
print(solve('AA', 26 - 1, None, 1))