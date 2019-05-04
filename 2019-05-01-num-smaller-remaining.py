# This problem was asked by Google.

# Given an array of integers, return a new array where each element in the new
# array is the number of smaller elements to the right of that element in the
# original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1

# 1,4 3,0 4,1 6,3 9,2
# 3,0

#    3
# 1     4
#          9
#         6


# Brute force
def transform_to_num_smaller_remaining(arr):
    result = []
    for i, x in enumerate(arr):
        result.append(sum([y < x for y in arr[i + 1:]]))

    return result

if __name__ == '__main__':
    L = [3, 4, 9, 6, 1]
    print("Should be [1, 1, 2, 1, 0]: ", transform_to_num_smaller_remaining(L))


# Notes: Better ways not coming to me right now.  Something involving sorting
# may be possible. This is O(n^2) right now. May revisit.

# Analysis: Yeah, I nearly had their solution in mind but lost it.  Start at
# right, maintain sorted list of elements seen, then bisect to see where each
# element would go in.
