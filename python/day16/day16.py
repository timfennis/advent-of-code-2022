import re
import sys
import functools

input = open(sys.argv[1] if len(sys.argv) >= 2 else 'input').read()

FLOW_RATES = dict()
NETWORK = dict()

for line in input.split('\n'):
    pipe, rate, connections = re.findall(r"Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? (.*)", line)[0]
    rate = int(rate)
    NETWORK[pipe] = connections.split(', ')
    FLOW_RATES[pipe] = rate

def unpack_nodes(n: str) -> set[str]:
    if n == '':
        return set()
    return set(n.split('.'))

def pack_nodes(n: set[str]):
    return '.'.join(sorted(list(n)))

@functools.cache
def solve(current_node: str, time: int, enp: str) -> list[int]:
    enabled_nodes = unpack_nodes(enp) 

    rate = sum([FLOW_RATES[node] for node in enabled_nodes])
    
    if time == 30:
        return []

    best_node = None
    best_solution = 0
    options = dict()
    
    # If the current node is not enabled AND it's flow rate is more than 0 consider enabling it
    if current_node not in enabled_nodes and FLOW_RATES[current_node] > 0:
        solution = [rate] + solve(current_node, time+1, pack_nodes(enabled_nodes.union(set([current_node]))))
        options[current_node] = solution
        
        # Make it our current best option
        best_node = current_node
        best_solution = sum(solution)

    # Look for other options
    for connected_node in NETWORK[current_node]:
        # Move to each connected node
        solution = [rate] + solve(connected_node, time+1, pack_nodes(enabled_nodes))
        options[connected_node] = solution

        if best_node is None or sum(solution) > best_solution:
            best_node = connected_node
            best_solution = sum(solution)

    assert best_node != None

    # Return the best option
    return options[best_node]

solution = solve('AA', 0, '')
print(solution)
print(sum(solution))