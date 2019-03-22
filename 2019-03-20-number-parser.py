# This problem was asked by LinkedIn.

# Given a string, return whether it represents a number. Here are the different
# kinds of numbers:

# "10", a positive integer
# "-10", a negative integer
# "10.1", a positive real number
# "-10.1", a negative real number
# "1e5", a number in scientific notation
# And here are examples of non-numbers:

# "a"
# "x 1"
# "a -2"
# "-"


def is_number(string):
    has_decimal = False
    has_digits = False

    if string[0] == "-":
        string = string[1:]

    # Note: intentionally allowing trailing decimal, as in JS, for example
    for i, c in enumerate(string):
        if not c.isdigit():
            if c == 'e':
                if i + 1 == len(string):
                    return False
                step = 2 if string[i + 1] == '-' else 1
                return string[i + step:].isdigit()
            elif c == '.':
                if has_decimal:
                    return False
                has_decimal = True
            else:
                return False

        else:
            has_digits = True

    return has_digits

if __name__ == '__main__':
    print("Should be True: ", is_number("10"))
    print("Should be True: ", is_number("-10"))
    print("Should be True: ", is_number("10.1"))
    print("Should be True: ", is_number("-10.1"))
    print("Should be True: ", is_number("1e5"))
    print("Should be True: ", is_number("1.5e5"))
    print("Should be True: ", is_number(".5e5"))
    print("Should be True: ", is_number(".5e-5"))
    print("Should be True: ", is_number(".55"))
    print("Should be True: ", is_number("-.5e5"))
    print("Should be True: ", is_number("5.e5"))
    print("Should be True: ", is_number("5."))

    print("Should be False: ", is_number("a"))
    print("Should be False: ", is_number("x 1"))
    print("Should be False: ", is_number("a -2"))
    print("Should be False: ", is_number("-"))
    print("Should be False: ", is_number("."))
    print("Should be False: ", is_number(".5.5"))
    print("Should be False: ", is_number("5e"))


# Notes: Went quite well: all cases passed on first go, and took maybe 20
# minutes or so.

# Analysis: Does in a single pass, whereas provided solution does multiple.
