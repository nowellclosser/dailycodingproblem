# This problem was asked by Google.

# You are in an infinite 2D grid where you can move in any of the 8 directions:

#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover
# the points. Give the minimum number of steps in which you can achieve it.
# You start from the first point.

# Example:

# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to
# move from (1, 1) to (1, 2).


def min_steps(points):

    def two_point_min(p1, p2):
        diagonal = min(abs(p2[1] - p1[1]), abs(p2[0] - p1[0]))
        cardinal = abs(p2[1] - p1[1]) + abs(p2[0] - p1[0]) - 2 * diagonal
        return diagonal + cardinal

    min_steps = 0
    for i in range(len(points) - 1):
        min_steps += two_point_min(points[i], points[i + 1])

    return min_steps

if __name__ == '__main__':
    print("Should be 2: ", min_steps([(0, 0), (1, 1), (1, 2)]))
    print("Should be 54: ", min_steps([(0, 0), (1, -2), (40, 50)]))


# Analysis: This works, but math can be simplified
# can just return max(abs(p2[1] - p1[1]), abs(p2[0] - p1[0]))
