# This problem was asked by Square.

# Assume you have access to a function toss_biased() which returns 0 or 1 with
# a probability that's not 50-50 (but also not 0-100 or 100-0). You do not
# know the bias of the coin.

# Write a function to simulate an unbiased coin toss.

import random


THRESHOLD = .02


def toss_biased():
    return int(random.random() < THRESHOLD)


def toss_unbiased():
    total_1 = 0
    total_2 = 0
    for _ in range(10000):
        total_1 += toss_biased()
        total_2 += toss_biased()

    return int(total_2 < total_1)


def toss_unbiased_efficient():
    coin1, coin2 = 0, 0

    while coin1 == coin2:
        coin1 = toss_biased()
        coin2 = toss_biased()

    return int(coin1 < coin2)

if __name__ == '__main__':
    total = 0
    for _ in range(100):
        total += toss_unbiased_efficient()

    print(total / 100)
