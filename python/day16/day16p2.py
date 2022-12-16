import re
import sys
import functools
from copy import copy

input = open(sys.argv[1] if len(sys.argv) >= 2 else 'example').read()

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
def solve(your_node: str, elepant_node: str, time: int, enp: str) -> list[int]:
    enabled_nodes = unpack_nodes(enp) 

    rate = sum([FLOW_RATES[node] for node in enabled_nodes])
    
    if time == 20:
        return []

    best_node = None
    best_solution = -1
    options = dict()
    
    # Look for other options
    for your_move in [your_node] + NETWORK[your_node]:
        for elephant_move in [elepant_node] + NETWORK[elepant_node]:
            new_nodes = copy(enabled_nodes)
            if your_move == your_node:
                # If opening the valve is a valuable move (it's not yet open, and gives more then 0 pressure)
                if FLOW_RATES[your_move] > 0 and your_move not in enabled_nodes:
                    new_nodes.add(your_node)
                else:
                    continue
            if elephant_move == elepant_node:
                # If opening the valve is a valuable move (it's not yet open, and gives more then 0 pressure)
                if FLOW_RATES[elephant_move] > 0 and elephant_move not in enabled_nodes:
                    new_nodes.add(elepant_node)
                else:
                    continue
            
            solution = [rate] + solve(your_move, elephant_move, time + 1, pack_nodes(new_nodes))
            solution_key = your_move + '.' + elephant_move
            options[solution_key] = solution
            solution_score = sum(solution)

            if solution_score > best_solution:
                best_node = solution_key
                best_solution = solution_score

    assert best_node != None

    # Return the best option
    return options[best_node]

solution = solve('AA', 'AA', 0, '')
print(solution)
print(sum(solution))