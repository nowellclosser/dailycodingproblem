# This question was asked by Google.

# Given an integer n and a list of integers l, write a function that randomly
# generates a number from 0 to n-1 that isn't in l (uniform).

import random


def constrained_randint(n, exclude_container):
    if type(exclude_container) is list:
        exclude_container = set(exclude_container)
    randint = random.randint(0, n - 1)
    if randint in exclude_container:
        return constrained_randint(n, exclude_container)

    return randint

if __name__ == '__main__':
    print("Should be 0:", constrained_randint(6, [1, 2, 3, 4, 5]))

    from collections import defaultdict
    results = defaultdict(int)
    for _ in range(10000):
        num = constrained_randint(10, [11, 8, 7, 6])
        results[num] += 1

    print("Should be uniformish fractions and not include 6,7,8: ")
    for num in results:
        print (num, results[num] / 10000)


# Analysis: Better to build up possible list and randomly sample from it- then
# only generating one random number.  This does depend on the relative size of
# n and l, though.  If n is much larger than length(n), might be ok to do this.

# I'm not sure what the complexity of random number generation is- OK it's
# constant time, but the worst case of this algorithm is still infinite since
# you can get infinitely unlucky.
