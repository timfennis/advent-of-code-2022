input = open('input').read()
def find_start(sequence: str, size: int) -> int:
    for idx in range(size, len(sequence)):
        if idx >= size:
            if len(set(sequence[idx-size:idx])) == size:
                return idx

assert find_start('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert find_start('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert find_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19

print(find_start(input, 4))
print(find_start(input, 14))