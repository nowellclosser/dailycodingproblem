# What does the below code snippet print out? How can we fix the anonymous
# functions to behave as we'd expect?

# functions = []
# for i in range(10):
#     functions.append(lambda: i)

# for f in functions:
#     print(f())


def broken():
    functions = []
    for i in range(10):
        functions.append(lambda: i)

    for f in functions:
        print(f())


def fixed():
    functions = []
    shared_range_iterator = iter(range(10))
    for _ in range(10):
        functions.append(lambda: next(shared_range_iterator))
    for f in functions:
        print(f())

if __name__ == '__main__':
    broken()
    fixed()


# Notes: This was tricky, and if I was only supposed to touch the lambda
# I'm not sure what to do. Probably wouldn't have passed an actual interview.

# Analysis: Can pass in named arguments to lambdas, which grabs pins i to its
# value at definition time: lambda i=i: i
