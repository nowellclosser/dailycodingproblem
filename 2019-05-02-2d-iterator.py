# This problem was asked by Uber.

# Implement a 2D iterator class. It will be initialized with an array of
# arrays, and should implement the following methods:

# next(): returns the next element in the array of arrays. If there are no more
# elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
# repeatedly should output 1, 2, 3, 4, 5, 6.

# Do not use flatten or otherwise clone the arrays. Some of the arrays can be
# empty.


class Iterator2D():
    def __init__(self, arr):
        self.arr = arr
        self.pos = [0, 0]

    def next(self):
        try:
            if len(self.arr[self.pos[0]]) == 0:
                self.pos[0] += 1
            result = self.arr[self.pos[0]][self.pos[1]]
            if self.pos[1] < len(self.arr[self.pos[0]]) - 1:
                self.pos[1] += 1
            else:
                self.pos[0] += 1
                self.pos[1] = 0
        except:
            raise StopIteration

        return result

    def has_next(self):
        return (self.pos[1] < len(self.arr[self.pos[0]]) or
                self.pos[0] < len(self.arr) or
                (len(self.arr[self.pos[0]]) == 0 and
                 self.pos[0] + 1 < len(self.arr)))

if __name__ == '__main__':
    it = Iterator2D([[1, 2], [3], [], [4, 5, 6]],)
    while True:
        print(it.next())


# While I could be more DRY, this is ok and of similar complexity to their
# solution.
