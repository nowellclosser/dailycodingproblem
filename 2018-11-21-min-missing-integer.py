# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def min_missing_pos_integer(arr):
    min_missing = 1
    for num in arr:
        if num == min_missing:



if __name__ == '__main__':
    print(min_missing_pos_integer([3,4,-1,1]))
