# This is your coding interview problem for today.

# Given a real number n, find the square root of n. For example, given n = 9,
# return 3.

THRESHOLD = .000001


def square_root(n):
    l = 0
    r = n
    possible_root = l + r / 2
    while (abs(possible_root * possible_root - n) > THRESHOLD):
        print(possible_root, l, r)
        if possible_root * possible_root > n:
            r = possible_root
        else:
            l = possible_root

        possible_root = (l + r) / 2

    return round(possible_root, 4)

if __name__ == '__main__':
    print("Should be 3.0: ", square_root(9))
    print("Should be 1.4142: ", square_root(2))

# Analysis: I know there is a sequence that converges to sqrt(n), but can't
# remember it, so using this as a reasonable, if not very clever, option.
