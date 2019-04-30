# This problem was asked by Facebook.

# Given an array of integers in which two elements appear exactly once and all
# other elements appear exactly twice, find the two elements that appear only
# once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
# The order does not matter.

# Follow-up: Can you do this in linear time and constant space?


def find_unique(arr):
    state = [0] * 32

    for num in arr:
        for i in range(len(state)):
            quotient = num // 2**(32 - i - 1)
            state[i] = (quotient + state[i]) % 2
            if quotient:
                num = num % quotient

    result = 0
    for i, val in enumerate(state):
        result += val * (2**(32 - i - 1))

    return result

if __name__ == '__main__':
    print(find_unique([2, 4, 6, 8, 10, 2, 6, 10]))


# Notes: This finds the sum of the two numbers... thinking about how to
# identify them separately.

# This is a very clever solution:

def array_two_elements(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num

    # Get rightmost set bit
    xor = xor & -xor

    rets = [0, 0]
    for num in arr:
        if num & xor:
            rets[0] = rets[0] ^ num
        else:
            rets[1] = rets[1] ^ num
    return rets
