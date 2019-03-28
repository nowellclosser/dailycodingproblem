# The Tower of Hanoi is a puzzle game with three rods and n disks, each a
# different size.

# All the disks start off on the first rod in a stack. They are ordered by
# size, with the largest disk on the bottom and the smallest one at the top.

# The goal of this puzzle is to move all the disks from the first rod to the
# last rod while following these rules:

# You can only move one disk at a time.
# A move consists of taking the uppermost disk from one of the stacks and
# placing it on top of another stack.
# You cannot place a larger disk on top of a smaller disk.
# Write a function that prints out all the steps necessary to complete the
# Tower of Hanoi. You should assume that the rods are numbered, with the first
# rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod
# being 3.

# For example, with n = 3, we can do this in 7 moves:

# Move 1 to 3
# Move 1 to 2
# Move 3 to 2
# Move 1 to 3
# Move 2 to 1
# Move 2 to 3
# Move 1 to 3


# 3
# 2
# 1
# x   x   x


# 2
# 1       3
# x   x   x


# 1   2   3
# x   x   x


#     3
# 1   2
# x   x   x


#     3
#     2   1
# x   x   x


# 3   2   1
# x   x   x


#         2
# 3       1
# x   x   x


#         3
#         2
#         1
# x   x   x

class Hanoi():
    def __init__(self, num_disks):
        self.state = [[x for x in range(num_disks)], [], []]
        self.count = 0

    def move_disk(self, src, dest):
        self.count += 1
        self.state[dest].append(self.state[src].pop())
        print("Move {} to {}".format(src + 1, dest + 1))

    def play(self, height=None, src=0, dest=2):
        if height is None:
            height = len(self.state[src])

        if height == 1:
            self.move_disk(src, dest)
            return

        scratch = ({0, 1, 2} - {src, dest}).pop()

        self.play(height - 1, src, scratch)

        self.move_disk(src, dest)

        self.play(height - 1, scratch, dest)


if __name__ == '__main__':
    game = Hanoi(5)
    game.play()
    print("Move count: {}".format(game.count))


# This took quite a while, but I'm very happy with the solution. Recurrence
# for runtime is T(n) = 2T(n) + 1.

# Analysis: Interestingly, you don't really need the state at all - just print
# that you're moving when you move.
