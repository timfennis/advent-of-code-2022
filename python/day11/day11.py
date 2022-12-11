from functools import partial
from math import lcm
from copy import deepcopy

monkeys = open('input').read().split("\n\n")

start_items = []
ops = []
divs = []
target = []

for monkey_index, monkey in enumerate(monkeys):
    start_items.append([])
    for line in monkey.split('\n'):
        if line.startswith("Monkey"):
            pass
        else:
            key, value = [it.strip() for it in line.split(": ")]
            if key == "Starting items":
                start_items[monkey_index] = [int(it) for it in value.split(', ')]
            elif key == "Operation":
                num = value.split(' ')[-1]
                if num == 'old':
                    ops.append(lambda x: x * x)
                elif '+' in value:
                    ops.append(partial(lambda y, x: x + y, int(num)))
                elif '*' in value:
                    ops.append(partial(lambda y, x: x * y, int(num)))
                else:
                    raise ValueError("Booooo")
            elif key == "Test":
                div = int(value.split(' ')[-1])
                divs.append(div)
            elif key == 'If true':
                on_true = int(value.split()[-1])
            elif key == 'If false':
                on_false = int(value.split()[-1])
            else:
                raise ValueError('Unexpected ', key)
    target.append((on_true, on_false))

l = lcm(*divs)
for part in [1,2]:
    inspections = [0 for _ in range(len(monkey))]
    items = deepcopy(start_items)
    for round in range(20 if part == 1 else 10000):
        for monkey_idx, sub_items in enumerate(items):
            for item in sub_items:
                inspections[monkey_idx] += 1
                new_level = ops[monkey_idx](item)
                if part == 1:
                    new_level = new_level // 3
                else:
                    new_level = new_level % l
                on_true, on_false = target[monkey_idx]
                if new_level % divs[monkey_idx] == 0:
                    items[on_true].append(new_level)
                else:
                    items[on_false].append(new_level)
            items[monkey_idx] = []

    a, b = sorted(inspections)[-2:]
    print(a * b)