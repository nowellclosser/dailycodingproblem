# This problem was asked by Jane Street.

# Generate a finite, but an arbitrarily large binary tree quickly in O(1).

# That is, generate() should return a tree whose size is unbounded but finite.

import random


class InfiniteNode():
    def __init__(self, val):
        self.val = val

    @property
    def left(self):
        return InfiniteNode(self.val)

    @property
    def right(self):
        return self.left


class UnboundedFiniteNode():
    def __init__(self, val):
        self.val = val
        self._left = None
        self._right = None

        self._left_evaluated = False
        self._right_evaluated = False

    @property
    def left(self):
        if not self._left_evaluated:
            if random.random() < .5:
                self._left = UnboundedFiniteNode(0)
            self._left_evaluated = True

        return self._left

    @property
    def right(self):
        if not self._right_evaluated:
            if random.random() < .5:
                self._right = UnboundedFiniteNode(0)
            self._right_evaluated = True

        return self._right


def generate():
    return UnboundedFiniteNode(0)


# Analysis: Not quite right- I was confused about the meaning of unbounded
# but finite.  In fact, I created an infinite, full tree, not realizing a tree
# of random, unbounded size was desired.  Easy fix, though, and got use of
# properties right, which is probably the key part.  Provided solution has
# slight messiness- providing left and right would allow them to be overwritten
# anyway.
