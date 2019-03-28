# This problem was asked by Facebook.

# Write a function that rotates a list by k elements. For example,
# [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving
# this without creating a copy of the list. How many swap or move operations do
# you need?


# Doesn't copy, or do complicated swapping. Does make a new list, though...
def rotate_list(source, k):
    if k % len(source) == 0:
        return source

    source[::] = [source[(i + k) % len(source)] for i in range(len(source))]

    # Just returning for simplified verification
    return source

if __name__ == '__main__':
    print("Should be [3, 4, 5, 6, 1, 2]: ", rotate_list([1, 2, 3, 4, 5, 6], 2))


# Analysis- better? than any of their solutions, but relies on a python trick
# whereas theirs are more general.  The reverse sublists and then reverse whole
# list trick is very clever, and lives up to only doing swapping.
