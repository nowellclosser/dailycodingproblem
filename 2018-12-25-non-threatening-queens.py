# This problem was asked by Microsoft.

# You have an N by N board. Write a function that, given N, returns the number
# of possible arrangements of the board where N queens can be placed on the
# board without threatening each other, i.e. no two queens share the same row,
# column, or diagonal.


def num_nonthreatening_arrangements(n):
    if n < 0:
        raise Exception("Invalid board size")
    if n < 2:
        return 0

    possible_arrangements = 0
    for column in range(n):
        available_spots = [(x, y) for x in range(n) for y in range(n)]
        placements = 1
        available_spots = remove_unavailable_spots(
            (0, column),
            available_spots
        )
        while placements < n and available_spots:
            placements += 1
            available_spots = remove_unavailable_spots(
                available_spots.pop(),
                available_spots
            )

        if placements == n:
            possible_arrangements += 1
            print("found one")

    return possible_arrangements


def remove_unavailable_spots(location, available_spots):
    print(location)
    still_available_spots = set()
    for x, y in available_spots:
        if (x == location[0] or y == location[1] or
                abs(location[0] - x) == abs(location[1] - y)):
            continue
        still_available_spots.add((x, y))

    return still_available_spots


# def num_nonthreatening_arrangements_v2(n):
#     if n < 0:
#         raise Exception("Invalid board size")
#     if n < 2:
#         return 0

#     possible_arrangements = 0
#     for column in range(n):
#         available_spots = [(x, y) for x in range(n) for y in range(n)]
#         placements = 1
#         available_spots = remove_unavailable_spots(
#             (0, column),
#             available_spots
#         )

#         possible_arrangements = recursive_helper(
#             available_spots,
#             n - placements
#         )

#     return possible_arrangements


# def recursive_helper(spots, placements):


if __name__ == '__main__':
    print(num_nonthreatening_arrangements(int(input())))


# Notes: Timer started ~5 min late. Took me a while to resort to brute force,
# after which this took about 40 min, but worked first try.

# Update: This breaks down at 6 because it only works on the first try starting
# at a particular location.  Can return max one for a given location and may
# miss all of them.
