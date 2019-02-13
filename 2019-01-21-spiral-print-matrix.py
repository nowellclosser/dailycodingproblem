# This problem was asked by Amazon.

# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

# For example, given the following matrix:

# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12


class SpiralPrinter:
    def __init__(self, matrix):
        self.matrix = matrix

        rows = len(matrix)
        cols = len(matrix[0])

        self.start_column = 0
        self.end_column = cols - 1

        self.start_row = 0
        self.end_row = rows - 1

    def _direction_generator(self):
        i = 0
        while True:
            yield ['R', 'D', 'L', 'U'][i % 4]
            i += 1

    def _print_direction(self, direction):
        if direction == 'R':
            for j in range(self.start_column, self.end_column + 1):
                print(self.matrix[self.start_row][j])
            self.start_row += 1
            return
        if direction == 'D':
            for j in range(self.start_row, self.end_row + 1):
                print(self.matrix[j][self.end_column])
            self.end_column -= 1
            return
        if direction == 'L':
            for j in range(self.end_column, self.start_column - 1, -1):
                print(self.matrix[self.end_row][j])
            self.end_row -= 1
            return
        if direction == 'U':
            for j in range(self.end_row, self.start_row - 1, -1):
                print(self.matrix[j][self.start_column])
            self.start_column += 1
            return

    def spiral_print(self):
        directions = self._direction_generator()
        while (self.start_column <= self.end_column and
               self.start_row <= self.end_row):
            self._print_direction(next(directions))

if __name__ == '__main__':
    SpiralPrinter([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]).spiral_print()
