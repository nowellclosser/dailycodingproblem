# This problem was asked by Uber.

# A rule looks like this:

# A NE B

# This means this means point A is located northeast of point B.

# A SW C

# means that point A is southwest of C.

# Given a list of rules, check if the sum of the rules validate. For example:

# A N B
# B NE C
# C N A
# does not validate, since A cannot be both north and south of C.

# A NW B
# A N B
# is considered valid.

from collections import defaultdict


def direction_rules_valid(filename):
    direction_record = defaultdict(lambda: defaultdict(set))

    with open(filename) as f:

        for line in f:
            tokens = line.rstrip().split(" ")
            p1 = tokens[0]
            directions = tokens[1]
            p2 = tokens[2]

            for d in directions:
                if path_exists(direction_record, p1, opposite(d), p2):
                    return False
                direction_record[d][p1].add(p2)
                direction_record[opposite(d)][p2].add(p1)

    return True


def path_exists(direction_record, p1, d, p2):
    # No cycles should exist, because the whole point of the check is to
    # preempt cycles.
    if p2 in direction_record[d][p1]:
        return True
    return any([path_exists(direction_record, p, d, p2)
               for p in direction_record[d][p1]])


def opposite(d):
    if d == "N":
        return "S"
    if d == "E":
        return "W"
    if d == "S":
        return "N"
    if d == "W":
        return "E"

if __name__ == '__main__':
    print("Should be True: ", direction_rules_valid("valid_rules_1.txt"))
    print("Should be False: ", direction_rules_valid("invalid_rules_1.txt"))
    print("Should be True: ", direction_rules_valid("valid_rules_2.txt"))
    print("Should be False: ", direction_rules_valid("invalid_rules_2.txt"))

# Notes: This took me way too long, almost 2 hours.  I didn't reduce it to
# the underlying graph problem until over an hour in, at which point luckily
# I realized I'd been constructing an adjacency set representation, but my
# initial approach of constructing all of the forbidden paths and deciding how
# to store those vs the actual recorded relationships slowed me down quite a
# bit. Happy with the ultimate solution though.


# Analysis: Should read solution more deeply- theirs is very similar but
# avoids recursion somehow, which would be nice...
