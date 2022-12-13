import functools
import math 

input = open('input').read()
groups = input.split('\n\n')

pairs = []
for index, pair in enumerate(groups):
    lines = pair.split('\n');
    eval("pairs.append((index, " + lines[0] + ", " + lines[1] + "))")

# There must be a way to express this more consicely right?
def validate(p1: list, p2: list):
    for a, b in zip(p1, p2):
        # If both A and B are lists we recurse
        if isinstance(a, list) and isinstance(b, list):
            result = validate(a, b)
            if result == True or result == False:
                return result
        # If both A and B are lists of lints we can do our cool comparison shiz
        elif isinstance(a, int) and isinstance(b, int):
            if a < b:
                return True
            elif a > b:
                return False
            else:
                pass 
        elif isinstance(a, int) and isinstance(b, list):
            result = validate([a], b)
            if result == True or result == False:
                return result
        elif isinstance(b, int) and isinstance(a, list):
            result = validate(a, [b])
            if result == True or result == False:
                return result
        else:
            raise ValueError("Unexpected types for a and b " + str(type(a)) + ", " + str(type(b)))

    # If no decission was made after comparing look at the lengths of the lists to see if
    # that is a tie breaker. If none of those happened we just return None and assume our
    # caller will handle the rest of the validation 
    if len(p1) > len(p2):
        return False
    elif len(p2) > len(p1):
        return True
    else:
        return None
    
valid_indexes = [index + 1 for index, p1, p2 in pairs if validate(p1, p2) == True]

print(sum(valid_indexes)) # should be 5852

cmp = functools.cmp_to_key(lambda a, b: -1 if validate(a, b) else 1)

sorted_pairs = [[[2]], [[6]]]
for _, p1, p2 in pairs:
    sorted_pairs.append(p1)
    sorted_pairs.append(p2)

sorted_pairs.sort(key=cmp)

indexes = [index + 1 for index, packet in enumerate(sorted_pairs) if packet in [[[2]], [[6]]]]
print(math.prod(indexes)) # should be 24190