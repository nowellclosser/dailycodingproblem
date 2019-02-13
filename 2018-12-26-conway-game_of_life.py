# This problem was asked by Dropbox.

# Conway's Game of Life takes place on an infinite two-dimensional board of
# square cells. Each cell is either dead or alive, and at each tick, the
# following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or
# diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a
# starting list of live cell coordinates and the number of steps it should run
# for. Once initialized, it should print out the board state at each step.
# Since it's an infinite board, print out only the relevant coordinates, i.e.
# from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a
# dot (.).

import copy


def game_of_life(coordinates, num_steps):
    if len(coordinates) < 2:
        raise Exception("There must be at least two living cells.")

    record = set()
    record.add(coordinates[0])

    min_x = max_x = coordinates[0][0]
    min_y = max_y = coordinates[0][1]
    for x, y in coordinates[1:]:
        record.add((x, y))
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    num_rows = max_x - min_x + 1
    num_cols = max_y - min_y + 1

    starting_board = []
    for row_num in range(num_rows):
        starting_board.append([])
        for col_num in range(num_cols):
            starting_board[row_num].append(
                '*' if (row_num + min_x, col_num + min_y) in record else '.'
            )
    print("Start state")
    print_board(starting_board)

    steps = 0
    board = starting_board
    while(steps < num_steps):
        print("Iteration", steps + 1)
        board = add_dead_border_if_necessary(board)
        frozen_board = copy.deepcopy(board)
        steps += 1

        for row_num, row in enumerate(frozen_board):
            for col_num, element in enumerate(frozen_board[row_num]):
                live_count = count_live_neighbors(
                    frozen_board, row_num, col_num
                )
                if element == '*':
                    if live_count < 2 or live_count > 3:
                        board[row_num][col_num] = '.'
                else:
                    if live_count == 3:
                        board[row_num][col_num] = '*'
        print_board(board)


def count_live_neighbors(frozen_board, row_num, col_num):
    count = 0
    for x in [row_num - 1, row_num, row_num + 1]:
        for y in [col_num - 1, col_num, col_num + 1]:
            if x == row_num and y == col_num:
                continue
            if x < 0 or x >= len(frozen_board):
                continue
            if y < 0 or y >= len(frozen_board[0]):
                continue

            if frozen_board[x][y] == '*':
                count += 1

    return count


def add_dead_border_if_necessary(board):
    if (all([x == '.' for x in board[0]]) and
            all([y == '.' for y in board[-1]]) and
            all(row[0] == row[-1] == '.' for row in board[1:-1])):
        return board

    for i in range(len(board)):
        board[i] = ['.'] + board[i] + ['.']
    return [['.'] * len(board[0])] + board + [['.'] * len(board[0])]


def print_board(board):
    max_x = max_y = 0
    min_x = len(board) - 1
    min_y = len(board[0]) - 1

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '*':
                if i < min_x:
                    min_x = i
                if i > max_x:
                    max_x = i
                if j < min_y:
                    min_y = j
                if j > max_y:
                    max_y = j

    for row in board[min_x: max_x + 1]:
        print(row[min_y: max_y + 1])

    print('\n')


if __name__ == '__main__':
    game_of_life([(1, 2), (1, 3), (1, 4), (2, 2), (2, 5)], 100)


# Notes: This took me several hours, though I was fairly organized. Waffled a
# bit on how to handle expansion outwards, and what I have now adds some
# borders that aren't needed.
