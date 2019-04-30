# This problem was asked by Google.

# Given an array of numbers and an index i, return the index of the nearest
# larger number of the number at index i, where distance is measured in array
# indices.

# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

# If two distances to larger numbers are the equal, then return any one of
# them.
# If the array at i doesn't have a nearest larger integer, then return null.

# Follow-up: If you can preprocess the array, can you do this in constant time?


def nearest_larger_idx(numbers, idx):

    for i in range(1, len(numbers)):
        if idx + i < len(numbers) and numbers[idx + i] > numbers[idx]:
            return idx + i
        if idx - i >= 0 and numbers[idx - i] > numbers[idx]:
            return idx - i

    return None

if __name__ == '__main__':
    print("Should be 3: ", nearest_larger_idx([4, 1, 3, 5, 6], 0))

# Notes: I don't really get the spirit of these preprocess questions usually,
# so just chose to see what they did.

# Analysis: The preprocess here can be to just go through and handle elements
# whose nearest larger number is adjacent. Then for nones use the above method.
