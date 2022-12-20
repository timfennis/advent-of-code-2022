from copy import copy

def mix(nums, o_nums):
    for o_num in o_nums:
        if (o_num[1] == 0):
            continue
        idx = nums.index(o_num)
        nums.remove(o_num)
        new_pos = (idx + o_num[1]) % len(nums)
        if new_pos == 0:
            nums.append(o_num)
        else:
            nums.insert(new_pos, o_num)
    return nums

def find_zero(nums):
    for idx, num in nums:
        if num == 0:
            return (idx, num)
    return None

def find_groove_coordinates(nums):
    zero = nums.index(find_zero(nums))
    s = 0
    for r in [1000,2000,3000]:
        s += nums[(zero + r) % len(nums)][1]
    return s

def solve(o_nums, mix_count, decryption_key):
    o_nums = [(i, n * decryption_key) for i, n in o_nums]
    nums = copy(o_nums)
    for _ in range(mix_count):
        nums = mix(nums, o_nums)

    return find_groove_coordinates(nums)

input = open('input').read()
nums = list(enumerate([int(it.strip()) for it in input.split('\n')]))

print(solve(nums, 1, 1))
print(solve(nums, 10, 811589153))