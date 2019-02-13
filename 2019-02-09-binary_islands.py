# This problem was asked by Amazon.

# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A
# 1 represents land and 0 represents water, so an island is a group of 1s that
# are neighboring whose perimeter is surrounded by water.

# For example, this matrix has 4 islands.

# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1

from collections import defaultdict

MAP = [[1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 0, 1],
       [1, 1, 0, 0, 1]]

FULL_MAP = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]


def count_islands(land_map):
    islands = 0
    visited = defaultdict(set)
    for i, row in enumerate(land_map):
        if len(visited[i]) == len(row):
            continue
        for j, pixel in enumerate(row):
            if (sum(len(s) for s in visited.values()) ==
                    len(land_map) * len(land_map[0])):
                return islands
            if j in visited[i]:
                continue
            if pixel:
                islands += 1
                explore_island(visited, land_map, i, j)

    return islands


def explore_island(visited, land_map, i, j):
    height = len(land_map)
    width = len(land_map[0])

    if ((not 0 <= i < height) or (not 0 <= j < width) or
            (not land_map[i][j]) or (j in visited[i])):
        return

    visited[i].add(j)

    explore_island(visited, land_map, i + 1, j)
    explore_island(visited, land_map, i + 1, j + 1)
    explore_island(visited, land_map, i, j + 1)
    explore_island(visited, land_map, i - 1, j + 1)
    explore_island(visited, land_map, i - 1, j)
    explore_island(visited, land_map, i - 1, j - 1)
    explore_island(visited, land_map, i, j - 1)
    explore_island(visited, land_map, i + 1, j - 1)

print("Should return 4", count_islands(MAP))

print("Should return 1", count_islands(FULL_MAP))


# Analysis- basically did it the same way as the solution, with a couple more
# early outs.  However, using a dict of sets for visited was silly, and I
# should have just used a 2D array.
