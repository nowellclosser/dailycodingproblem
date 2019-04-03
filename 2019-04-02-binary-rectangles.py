# This question was asked by Google.

# Given an N by M matrix consisting only of 1's and 0's, find the largest
# rectangle containing only 1's and return its area.

# For example, given the following matrix:

# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
# Return 4.

from collections import defaultdict


def largest_block(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # record what rectangles exist organized by the bottom right corner
    rectangle_tracker = RectangleTracker()

    for i in range(num_rows):
        for j in range(num_cols):
            if not matrix[i][j]:
                continue

            rectangle_tracker.record(i, j, i, j)

            for u, v in rectangle_tracker.get(i, j - 1):
                if u == i or (u, j) in rectangle_tracker.get(i - 1, j):
                    rectangle_tracker.record(i, j, u, v)

            for u, v in rectangle_tracker.get(i - 1, j):
                if v == j or (i, v) in rectangle_tracker.get(i, j - 1):
                    rectangle_tracker.record(i, j, u, v)

    return rectangle_tracker.max_area


class RectangleTracker():
    def __init__(self):
        self.tracker = defaultdict(set)
        self.max_area = 0

    def record(self, br, bc, tr, tc):
        self.tracker[(br, bc)].add((tr, tc))

        area = (br - tr + 1) * (bc - tc + 1)
        if area > self.max_area:
            self.max_area = area

    def get(self, i, j):
        return self.tracker[(i, j)]

if __name__ == '__main__':

    MATRIX_1 = [[1, 0, 0, 0],
                [1, 0, 1, 1],
                [1, 0, 1, 1],
                [0, 1, 0, 0]]
    print("Should be 4: ", largest_block(MATRIX_1))

    MATRIX_2 = [[1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 1, 0, 0]]
    print("Should be 8: ", largest_block(MATRIX_2))

    MATRIX_3 = [[1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 1, 1],
                [0, 1, 1, 1]]
    print("Should be 6: ", largest_block(MATRIX_3))

    MATRIX_4 = [[1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 1, 0],
                [0, 1, 1, 1]]
    print("Should be 4: ", largest_block(MATRIX_4))

    MATRIX_5 = [[1, 0, 0, 0],
                [0, 0, 0, 1],
                [1, 0, 1, 0],
                [0, 1, 0, 1]]
    print("Should be 1: ", largest_block(MATRIX_5))

    MATRIX_6 = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    print("Should be 0: ", largest_block(MATRIX_6))

    MATRIX_7 = [[1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]]
    print("Should be 16: ", largest_block(MATRIX_7))


# Analysis: Uses more space than their solution, which is a clever way to
# just keep a cache the size of a row collecting streaks of 1s, and deducing
# areas from that along the way.
