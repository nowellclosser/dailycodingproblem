# This problem was asked by Google.

# Find the minimum number of coins required to make n cents.

# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢,
# and a 1¢.

from math import inf

DENOMINATIONS = {1, 5, 10, 25}


def min_coins_recursive(n):
    if n < 0:
        return inf

    if n == 0:
        return 0

    return min([min_coins_recursive(n - x) for x in DENOMINATIONS]) + 1


def min_coins(n):
    min_coins = [None] * (n + 1)
    min_coins[0] = 0
    for i in range(1, n + 1):
        if i in DENOMINATIONS:
            min_coins[i] = 1
        else:
            min_coins[i] = min([min_coins[i - x]
                                if i - x > 0 and min_coins[i - x] else inf
                                for x in DENOMINATIONS]) + 1
    return min_coins[n]

if __name__ == '__main__':
    print("Should be 3: ", min_coins_recursive(16))
    print("Should be 2: ", min_coins_recursive(30))
    # print("Should be 4: ", min_coins_recursive(100)) Already slow!

    print("Should be 3: ", min_coins(16))
    print("Should be 2: ", min_coins(30))
    print("Should be 4: ", min_coins(100))
    print("Should be 41: ", min_coins(1001))

# Notes: I knew the DP was superior but just wanted to write both.
