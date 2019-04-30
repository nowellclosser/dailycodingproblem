# This problem was asked by Jane Street.

# Given an arithmetic expression in Reverse Polish Notation, write a program to
# evaluate it.

# The expression is given as a list of numbers and operands. For example:
# [5, 3, '+'] should return 5 + 3 = 8.

# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
# should return 5, since it is equivalent to
# ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# You can assume the given expression is always valid.
import operator

EXPRESSION_MAP = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def evaluate_rpn(expr):
    num_stack = []

    for token in expr:
        if token in EXPRESSION_MAP:
            right = num_stack.pop()
            left = num_stack.pop()
            num_stack.append(EXPRESSION_MAP[token](left, right))
        else:
            num_stack.append(token)

    return num_stack[0]

if __name__ == '__main__':
    print("Should be 5.0: ", evaluate_rpn(
        [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])
    )
