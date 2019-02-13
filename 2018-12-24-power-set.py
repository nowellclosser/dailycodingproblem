# This problem was asked by Google.

# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return
# {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.


def power_set(arr):
    if len(arr) == 1:
        return [[], arr]
    result = []
    for i, num in enumerate(arr):
        for subset in power_set(arr[:i] + arr[i + 1:]):
            result += [[num] + subset, subset]

    return result[:2 ** len(arr)]


def power_set_redo(arr):
    if len(arr) == 0:
        return [[]]

    result = []
    for subset in power_set_redo(arr[1:]):
        result.extend([[arr[0]] + subset, subset])

    return result

if __name__ == '__main__':
    print(power_set([1, 2, 3]))
    print(power_set_redo([1, 2, 3]))


# Notes: The janky solution took me 38 minutes.  If I knew how to generate all
# permutations of a set I could just generate binary permutations that
# correspond to each subset, with 0...n ones in the sequences that need to
# be permuted.

# It was coincidental that the first 2 ^ n subsets generated are unique.  Need
# to think about why that is and not generate the others in the first place.

# Update: can simply look at the first element, as was my initial intuition.
