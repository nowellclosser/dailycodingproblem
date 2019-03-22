# This question was asked by Zillow.

# You are given a 2-d matrix where each cell represents number of coins in that
# cell. Assuming we start at matrix[0][0], and can only move right or down,
# find the maximum number of coins you can collect by the bottom right corner.

# For example, in this matrix

# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.

# Brute force solution is to consider all m + n choose n paths.
# Dynamic programming solution can build up solution in O(n^2) time instead.


def max_coins(coin_matrix):
    m = len(coin_matrix)
    n = len(coin_matrix[0])

    max_coins_from_location = [[0 for _ in range(n)] for __ in range(m)]

    max_coins_from_location[m - 1][n - 1] = coin_matrix[m - 1][n - 1]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            right_coins = 0
            down_coins = 0
            if j + 1 < n:
                right_coins = max_coins_from_location[i][j + 1]
            if i + 1 < m:
                down_coins = max_coins_from_location[i + 1][j]
            max_coins_from_location[i][j] = (
                coin_matrix[i][j] + max(right_coins, down_coins)
            )

    for row in max_coins_from_location:
        print(row)

    return max_coins_from_location[0][0]

if __name__ == '__main__':
    COIN_MATRIX = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1],
    ]

    print("Should be 12", max_coins(COIN_MATRIX))


# Analysis- They did this recursively, interestingly.  Either way it's O(MN).
# But I'm happy with this. Only thing I'd change is starting at top left
# instead of bottom right.
