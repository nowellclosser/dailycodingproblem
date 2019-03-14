# This problem was asked by Palantir.

# Given a number represented by a list of digits, find the next greater
# permutation of a number, in terms of lexicographic ordering. If there is not
# greater permutation possible, return the permutation with the lowest
# value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should
# return [2,1,3]. The list [3,2,1] should return [1,2,3].

# Can you perform the operation without allocating extra memory
# (disregarding the input memory)?

# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4


def next_permutation(number):

    def helper(number):
        if len(number) < 2:
            return number, True

        if len(number) == 2:
            if number[0] < number[1]:
                number[0], number[1] = number[1], number[0]
                return number, True

            return number, False

        rest, found_next = helper(number[1:])

        if found_next:
            return [number[0]] + rest, True

        if number[0] > number[1]:
            return number, False

        number = [number[0]] + number[1:][::-1]
        number[0], number[1] = number[1], number[0]
        return number, True

    number, found_next = helper(number)
    if found_next:
        return number

    return number[::-1]

if __name__ == '__main__':
    print("Should be [1, 3, 2]", next_permutation([1, 2, 3]))
    print("Should be [2, 1, 3]", next_permutation([1, 3, 2]))
    print("Should be [1, 2, 3, 4]", next_permutation([4, 3, 2, 1]))
    print("Should be [2, 1, 3, 4]", next_permutation([1, 4, 3, 2]))
    print("Should be [1, 4, 2, 3, 5]", next_permutation([1, 3, 5, 4, 2]))


# Notes: definitely don't love this solution. Curious how they did it.

# Not quite right- if next highest value to pivot isn't end of list, breaks.
# Need to redo
