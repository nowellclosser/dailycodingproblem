# This problem was asked by Google.

# Given an array of integers where every integer occurs three times except for
# one integer, which only occurs once, find and return the non-duplicated
# integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13],
# return 19.

# Do this in O(N) time and O(1) space.


# Scratch: O(1) space is the hard part.
# There are (N-1)/3 + 1 = O(N) distinct #s

from collections import defaultdict


def return_non_duplicated_integer(numbers):
    record = defaultdict(int)
    for x in numbers:
        if record[x] == 2:
            del record[x]
        else:
            record[x] += 1

    return next(iter(record))


def solution_from_memory(numbers):
    record = [0] * 32
    for num in numbers:
        for i in range(32):
            bit = num >> i & 1
            record[i] = (record[i] + bit) % 3

    result = 0
    for i, bit in enumerate(record):
        result += bit * 2 ** i

    return result

if __name__ == '__main__':
    print(return_non_duplicated_integer([6, 1, 3, 3, 3, 6, 6, 1, 1, 7]))
    print(solution_from_memory([6, 1, 3, 3, 3, 6, 6, 1, 1, 7]))

# Notes: 16 m. Not constant space though.

# Update: yeah have to bit fiddle for constant time.
