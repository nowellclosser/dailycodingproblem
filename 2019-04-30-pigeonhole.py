# This problem was asked by Google.

# You are given an array of length n + 1 whose elements belong to the set
# {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
# Find it in linear time and space.


def find_duplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

if __name__ == '__main__':
    print("Should be 3:", find_duplicate([1, 2, 4, 3, 5, 3]))


# Analysis: Maybe there was a typo in the problem spec?
# The solutions both require constant space, and the second assumes there
# is exactly one duplicate.  In any case, the first is clever and
# involves checking if arr[i]= i.  If not, and arr[i]= j, we swap arr[i] and
# arr[j] unless arr[i] and arr[j] are equal, in which case we return the
# element.
