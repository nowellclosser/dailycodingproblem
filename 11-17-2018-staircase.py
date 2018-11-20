# There's a staircase with N steps, and you can climb 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb
# the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could
# climb any number from a set of positive integers X? For example, if
# X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
# Generalize your function to take in X.


# Scratch:
# 1 -> 1
# 1

# 2 -> 2
# 1 1
# 2

# 3 -> 3
# 1 1 1
# 1 2
# 2 1

# 4 -> 5
# 1 1 1 1
# 2 1 1
# 1 2 1
# 1 1 2
# 2 2

# 5 -> 8
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 2 2 1
# 2 1 2
# 1 2 2

# 6 -> 13
# 1 1 1 1 1 1
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2
# 2 2 1 1
# 1 2 2 1
# 1 1 2 2
# 2 1 2 1
# 2 1 1 2
# 1 2 1 2
# 2 2 2


# f(n) = f(n-1) + f(n-2), ie fibonacci!

CACHED_NUM_ROUTES = {}

def num_routes(num_steps):
    ''' This is just memoized fibonacci '''
    if CACHED_NUM_ROUTES.get(num_steps):
        return CACHED_NUM_ROUTES[num_steps]
    if num_steps in (1,2):
        return num_steps

    result1 = num_routes(num_steps - 1)
    result2 = num_routes(num_steps - 2)

    result = result1 + result2
    CACHED_NUM_ROUTES[num_steps] = result
    return result


CACHED_NUM_ROUTES_GENERALIZED = {}
def num_routes_generalized(num_steps, intervals):
    ''' This is ordered make change '''

    if CACHED_NUM_ROUTES_GENERALIZED.get(num_steps):
        return CACHED_NUM_ROUTES_GENERALIZED[num_steps]

    if num_steps < min(intervals):
        return 0;

    result = sum([num_routes_generalized(num_steps - interval, intervals)
                for interval in intervals])

    if num_steps in intervals:
        result += 1

    CACHED_NUM_ROUTES_GENERALIZED[num_steps] = result
    return result

if __name__ == '__main__':
    GENERALIZED_INTERVALS = [3,5]
    print("How many steps?")
    num_steps = int(input())
    print("num routes with fixed interval [1, 2]:")
    print(num_routes(num_steps))
    print("num routes with generalized interval:", GENERALIZED_INTERVALS)
    print(num_routes_generalized(num_steps, GENERALIZED_INTERVALS))

# Provided solutions:
def staircase_1(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

def staircase_2(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]







