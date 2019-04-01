# This problem was asked by Facebook.

# Given an array of numbers representing the stock prices of a company in
# chronological order and an integer k, return the maximum profit you can make
# from k buys and sells. You must buy the stock before you can sell it, and you
# must sell the stock before you can buy it again.

# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.


def max_return(prices, k):

    CACHE = [[None for _ in range(len(prices))] for _ in range(k + 1)]

    def max_helper(k, index):
        nonlocal CACHE
        nonlocal prices

        if index >= len(prices) or k <= 0:
            return 0

        max_sum = float("-inf")
        for i in range(index, len(prices)):
            if len(prices[i:]) < (2 * k):
                break
            if CACHE[k][i] is not None:
                return CACHE[k][i]
            for j in range(i + 1, len(prices)):
                if len(prices[j + 1:]) < (2 * (k - 1)):
                    break
                result = prices[j] - prices[i] + max_helper(k - 1, j + 1)
                if result > max_sum:
                    max_sum = result

        CACHE[k][index] = max_sum
        return max_sum
    return max_helper(k, 0)


if __name__ == '__main__':
    print("Should be 3: ", max_return([5, 2, 4, 0, 1], 2))
    print("Should be 6: ", max_return([5, 2, 4, 10, 12, 10], 2))
    print("Should be -inf: ", max_return([5, 2, 4, 10, 12, 10], 8))
    print("Should be 10: ", max_return([5, 2, 4, 10, 12, 10], 1))
    print("Should be 1: ", max_return([5, 2, 4, 10, 12, 10], 3))


# Notes: This took too long, and I get the feeling it's uglier than it
# needs to be.

# Analysis: I think this ends up similar to theirs, but it's not clean, and
# I would benefit from redoing as a cleaner DP problem.
