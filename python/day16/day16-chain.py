import re
import sys
import functools
from copy import copy

input = open(sys.argv[1] if len(sys.argv) >= 2 else 'input').read()

FLOW_RATES = dict()
NETWORK = dict()

for line in input.split('\n'):
    pipe, rate, connections = re.findall(r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)[0]
    rate = int(rate)
    NETWORK[pipe] = connections.split(', ')
    FLOW_RATES[pipe] = rate

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
    for connected_node in NETWORK[current_node]:
        best = max(best, solve(connected_node, time_remaining-1, enabled_nodes, players_remaining))
    
    return best

print(solve('AA', 30 - 1, None, 0))
print(solve('AA', 26 - 1, None, 1))