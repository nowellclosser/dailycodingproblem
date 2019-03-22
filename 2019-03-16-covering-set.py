# This problem was asked by Google.

# Given a set of closed intervals, find the smallest set of numbers that covers
# all the intervals. If there are multiple smallest sets, return any of them.

# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
# numbers that covers all these intervals is {3, 6}.


def smallest_covering_set(intervals):

    unprocessed_intervals = set(tuple(l) for l in intervals)
    reduced_intervals = []

    while unprocessed_intervals:
        cur = unprocessed_intervals.pop()
        for compare in unprocessed_intervals.copy():
            overlap = _overlap(cur, compare)
            if overlap:
                unprocessed_intervals.remove(compare)
                cur = overlap
        reduced_intervals.append(cur)

    return [interval[0] for interval in reduced_intervals]


def _overlap(l, r):
    possible_lower = max(l[0], r[0])
    possible_upper = min(r[1], r[1])

    if possible_lower <= possible_upper:
        return [possible_lower, possible_upper]

    return []


if __name__ == '__main__':
    print(
        "Should be [6, 3]: ",
        smallest_covering_set([[0, 3], [2, 6], [3, 4], [6, 9]])
    )
