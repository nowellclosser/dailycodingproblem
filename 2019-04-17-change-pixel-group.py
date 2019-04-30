# Given a 2-D matrix representing an image, a location of a pixel in the screen
# and a color C, replace the color of the given pixel and all adjacent same
# colored pixels with C.

# For example, given the following matrix, and location pixel of (2, 2), and
# 'G' for green:

# B B W
# W W W
# W W W
# B B B

# Becomes

# B B G
# G G G
# G G G
# B B B


def change_adjacent_pixels(image, x, y, color, start_color=None):
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
        return

    start_color = start_color or image[x][y]

    if color == start_color:
        return

    if image[x][y] == start_color:
        image[x][y] = color
        change_adjacent_pixels(image, x, y + 1, color, start_color)
        change_adjacent_pixels(image, x + 1, y, color, start_color)
        change_adjacent_pixels(image, x, y - 1, color, start_color)
        change_adjacent_pixels(image, x - 1, y, color, start_color)

if __name__ == '__main__':
    IMAGE = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B'],
    ]

    DESIRED_RESULT = [
        ['B', 'B', 'G'],
        ['G', 'G', 'G'],
        ['G', 'G', 'G'],
        ['B', 'B', 'B'],
    ]

    change_adjacent_pixels(IMAGE, 2, 2, 'G')

    print("Should be: ")
    for row in DESIRED_RESULT:
        print(row)
    print("\nIs: ")
    for row in IMAGE:
        print(row)

# Notes: Not allowing purely diagonal adjacency
# Could (should) add a visited matrix to limit some of the steps. Exponential
# as is.

# Analysis: Yeah, this plus visited is the way they did it.
