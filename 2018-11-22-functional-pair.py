# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
# and last element of that pair. For example, car(cons(3, 4)) returns 3, and
# cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.

def get_first_element(a, b):
    return a

def get_second_element(a, b):
    return b

def car(pair):
    return pair(get_first_element)

def cdr(pair):
    return pair(get_second_element)

if __name__ == '__main__':
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
