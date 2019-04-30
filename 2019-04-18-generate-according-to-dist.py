# This problem was asked by Triplebyte.

# You are given n numbers as well as n probabilities that sum up to 1. Write a
# function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities
# [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50%
# of the time, and 3 and 4 20% of the time.

# You can generate random numbers between 0 and 1 uniformly.

import random
from collections import defaultdict


def random_choice_with_distribution(numbers, weights):

    rand = random.random()

    cum_weight = 0
    for i, weight in enumerate(weights[:-1]):
        cum_weight += weight
        if rand < cum_weight:
            return numbers[i]

    return numbers[-1]

if __name__ == '__main__':
    counts = defaultdict(int)
    for i in range(1000):
        num = random_choice_with_distribution(
            [1, 2, 3, 4],
            [0.1, 0.5, 0.2, 0.2]
        )
        counts[num] += 1

    print(counts)


# Notes: Very easy one for me, maybe 5 min

# Analysis: They also gave a preprocess solution on the probabilities, which
# I considered, but it doesn't really make sense to me given the inputs. In
# that case, you can binary search on the already summed probs.
