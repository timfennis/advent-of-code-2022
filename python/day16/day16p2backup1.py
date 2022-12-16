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

FINAL_RATE = sum(FLOW_RATES.values())

def unpack_nodes(n: str) -> set[str]:
    if n == '':
        return set()
    return set(n.split('.'))

def pack_nodes(n: set[str]):
    return '.'.join(sorted(list(n)))

def find_valuable_nodes(source: str, depth: int, excluding: list[str]) -> list[tuple[str, int]]:
    output = dict()
    for connected_node in NETWORK[source]:
        if connected_node in excluding:
            continue
        if FLOW_RATES[connected_node] > 0:
            output[connected_node] = depth
        else:
            for (new_node, distance) in find_valuable_nodes(connected_node, depth + 1, excluding + [connected_node]):
                if new_node in output and output[new_node] > distance:
                    output[new_node] = distance
                elif new_node not in output:
                    output[new_node] = distance


    return output.items()

@functools.cache
def solve(yp: str, ep: str, time: int, enp: str) -> list[int]:
    your_path = yp.split('.')
    elephant_path = ep.split('.')
    enabled_nodes = unpack_nodes(enp) 

    rate = sum([FLOW_RATES[node] for node in enabled_nodes])
    
    if time == 26:
        return []

    if rate == FINAL_RATE:
        return [FINAL_RATE] * (26 - time)

    best_node = None
    best_solution = -1
    options = dict()

    your_node = your_path[-1]
    elephant_node = elephant_path[-1] 
    # Look for other options
    for your_move in [your_node] + NETWORK[your_node]:
        for elephant_move in [elephant_node] + NETWORK[elephant_node]:
            new_nodes = copy(enabled_nodes)
            if your_move == your_node:
                # If opening the valve is a valuable move (it's not yet open, and gives more then 0 pressure)
                if FLOW_RATES[your_move] > 0 and your_move not in enabled_nodes:
                    your_path = [] # Clear the path
                    new_nodes.add(your_node)
                else:
                    continue
            else:
                if your_move in your_path:
                    continue
            if elephant_move == elephant_node:
                # If opening the valve is a valuable move (it's not yet open, and gives more then 0 pressure)
                if FLOW_RATES[elephant_move] > 0 and elephant_move not in enabled_nodes:
                    elephant_path = [] # Clear the path
                    new_nodes.add(elephant_node)
                else:
                    continue
            else:
                if elephant_move in elephant_path:
                    continue
            
            solution = [rate] + solve('.'.join(your_path + [your_move]), '.'.join(elephant_path + [elephant_move]), time + 1, pack_nodes(new_nodes))
            solution_key = your_move + '.' + elephant_move
            options[solution_key] = solution
            solution_score = sum(solution)

            if solution_score > best_solution:
                best_node = solution_key
                best_solution = solution_score
    if best_node == None:
        # In this case pick the retarded option
        return [rate] + solve(yp + '.' + your_move, ep + '.' + elephant_move, time + 1, pack_nodes(enabled_nodes))

    assert best_node != None

    # Return the best option
    return options[best_node]

solution = solve('AA', 'AA', 0, '')
print(solution)
print(sum(solution))