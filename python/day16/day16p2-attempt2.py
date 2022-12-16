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
                key = source + '.' + new_node
                if key in output and output[key] > distance:
                    output[key] = distance
                elif new_node not in output:
                    output[key] = distance


    return output.items()

# print(find_valuable_nodes('AA', 1, []))
# exit()

@functools.cache
def solve(your_node: str, elephant_node: str, time: int, enp: str) -> list[int]:
    enabled_nodes = unpack_nodes(enp) 

    rate = sum([FLOW_RATES[node] for node in enabled_nodes])
    
    if time == 26:
        return []

    if rate == FINAL_RATE:
        return [FINAL_RATE] * (26 - time)

    best_node = None
    best_solution = -1
    options = dict()

    # Look for other options
    your_options = [your_node] if your_node not in enabled_nodes and FLOW_RATES[your_node] > 0 else []
    elephant_options = [elephant_node] if elephant_node not in enabled_nodes and FLOW_RATES[elephant_node] > 0 else []

    your_options += NETWORK[your_node]
    elephant_options += NETWORK[elephant_node]

    for your_move in your_options:
        for elephant_move in elephant_options:
            if your_move in enabled_nodes and len(NETWORK[your_move]) == 1:
                continue

            if elephant_move in enabled_nodes and len(NETWORK[elephant_move]) == 1:
                continue
            
            new_nodes = enabled_nodes
            if your_move == your_node:
                new_nodes = copy(enabled_nodes)
                new_nodes.add(your_node)
            if elephant_move == elephant_node:
                new_nodes = copy(enabled_nodes)
                new_nodes.add(elephant_node)
            
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