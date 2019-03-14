# This problem was asked by Coursera.

# Given a 2D board of characters and a word, find if the word exists in the
# grid.

# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.

# For example, given the following board:

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true,
# exists(board, "ABCB") returns false.


def exists(board, word):

    def helper(word, i, j, visited):
        if (not 0 <= i < len(board)) or (not 0 <= j < len(board[0])):
            return False

        if visited[i][j]:
            return False

        if len(word) == 1:
            return board[i][j] == word

        if board[i][j] != word[0]:
            return False

        visited[i][j] = True

        found = any([
            helper(word[1:], i + 1, j, visited),
            helper(word[1:], i, j + 1, visited),
            helper(word[1:], i - 1, j, visited),
            helper(word[1:], i, j - 1, visited)
        ])

        if not found:
            visited[i][j] = False

        return found

    visited = [[0] * len(board[False]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if helper(word, i, j, visited):
                return True

    return False

if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print("Should be True", exists(board, "ABCCED"))
    print("Should be False", exists(board, "ESEF"))
    print("Should be True", exists(board, "CCEESE"))
    print("Should be False", exists(board, "CSECC"))
    print("Should be True", exists(board, "SEE"))
