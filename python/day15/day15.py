import re
from functools import reduce
from copy import deepcopy

input = open('input').read()

def m_distance(sx, sy, bx, by):
    return abs(sx - bx) + abs(sy - by)

def merge(a: range, b: range):
    if b.start <= a.stop <= b.stop:
        return [range(min(a.start, b.start), b.stop)]
    elif a.start <= b.stop <= a.stop:
        return [range(min(a.start, b.start), a.stop)]
    else:
        return [a, b]

def merge_all(ranges: list[range]):
    start = len(ranges)
    merged = []
    for r in ranges:
        if len(merged) == 0:
            merged = [r]
        else:
            last = merged[-1]
            merged[-1:] = merge(r, last)

    end = len(merged)
    if start == end:
        return merged
    else:
        return merge_all(merged)
sensors = []
beacons = set()

for line in input.split('\n'):
    sx, sy, bx, by = [int(it) for it in re.findall(r'(-?\d+)+', line)]

    sensors.append((sx, sy, m_distance(sx, sy, bx, by)))
    beacons.add((bx, by))

# cannot_contain = 0
# for x in range(-25000000, 25000000):
#     y = 2000000

#     for (sx, sy, sd) in sensors:
#         if m_distance(x, y, sx, sy) <= sd and (x,y) not in beacons:
#             cannot_contain += 1
#             break

# print(cannot_contain)

y_dict = dict()
for y in range(4_000_000):
    ranges = []
    for (sx, sy, sd) in sensors:
        distance = m_distance(sx, y, sx, sy)
        
        ydiff = abs(y - sy)
        if ydiff < sd:
            range_radius = sd - ydiff 
            x_range = range(sx - range_radius, sx + range_radius + 1)
            ranges.append(x_range)

    ranges = sorted(ranges, key=lambda x: x.stop)

    merged = merge_all(ranges)
    
    if (len(merged) != 1):
        # print("DID NOT REDUCE FURTHER", merged, y)
        print(merged[1].stop * 4_000_000 + y)
        exit()
    
    
    
