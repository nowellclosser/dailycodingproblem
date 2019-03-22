# This problem was asked by Microsoft.

# You have n fair coins and you flip them all at the same time. Any that come
# up tails you set aside. The ones that come up heads you flip again. How many
# rounds do you expect to play before only one coin remains?

# Write a function that, given n, returns the number of rounds you'd expect to
# play until one coin remains.

import math


def expected_rounds(num_coins):
    return math.ceil(math.log(num_coins, 2))

# This gives the number of rounds where the expected number of rounds is below
# 1. Perhaps it should go until number is less than 2 or rounds to 1?
