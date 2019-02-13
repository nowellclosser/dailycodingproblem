# This problem was asked by Google.

# Given a string of parentheses, write a function to compute the minimum
# number of parentheses to be removed to make the string valid (i.e. each open
# parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1. Given the
# string ")(", you should return 2, since we must remove all of them.


def min_removals(paren_string):
    unmatched_rights = 0
    unmatched_lefts = 0
    for char in paren_string:
        if char == "(":
            unmatched_lefts += 1
        elif char == ")":
            if unmatched_lefts:
                unmatched_lefts -= 1
            else:
                unmatched_rights += 1
        else:
            raise Exception("Really weird character for sure!")

    return unmatched_lefts + unmatched_rights


if __name__ == '__main__':
    print("Should be 1", min_removals("()())()"))
    print("Should be 2", min_removals(")("))
    print("Should be 0", min_removals("()()"))
    print("Should be 0", min_removals("(((((())))))(())()()"))
    print("Should be 6", min_removals("(((((("))
    print("Should be 4", min_removals("())))()("))


# Performance notes: < 10 minutes probably, not counting tests.  Pretty easy
# one.

# Analysis: Solution almost exactly like official- thumbs up!
