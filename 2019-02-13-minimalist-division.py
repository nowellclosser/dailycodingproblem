# This question was asked by ContextLogic.

# Implement division of two positive integers without using the division,
# multiplication, or modulus operators. Return the quotient as an integer,
# ignoring the remainder.


def divide(a, b):
    if (b == 0):
        return None
    remainder = a
    quotient = 0
    while remainder >= b:
        remainder -= b
        quotient += 1

    return quotient

if __name__ == '__main__':
    print("Should be 57: ", divide(400, 7))
    print("Should be 0: ", divide(1, 7))
    print("Should be 1: ", divide(1, 1))
    print("Should be None: ", divide(1, 0))

# Notes: extremely easy- 6 minutes including testing. And zero handling was a
# good catch.
