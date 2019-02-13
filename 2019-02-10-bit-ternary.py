# This problem was asked by Facebook.

# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or
# 0.

# Need to implement x if b == 1 else y.
# I'm slightly unclear on what is allowed, but obviously no conditionals.
# Loops or storage in in arrays though?

# single bit version
# def pick_based_on_bit(x, y, b):
#     return (x & b) + (y & ~b + 2)

# x & (00000000... if b = 0, 11111111... if b = 1)
# y & (11111111... if b = 0, 00000000... if b = 1)


def pick_based_on_bit(x, y, b):
    return (x & -b) + (y & -(~b + 2))

print("Should be 95555555, 78, 78, 95555555")
print(pick_based_on_bit(95555555, 78, 1))
print(pick_based_on_bit(95555555, 78, 0))
print(pick_based_on_bit(78, 95555555, 1))
print(pick_based_on_bit(78, 95555555, 0))

# Analysis- got a bit too excited about bit operations- can just do
# return (x * b) | (y * (1 - b))
# + or | work.

# Also ~b + 2 is a really dumb thing to do instead of 1 - b. Again, hung up on
# bit operations.
