# This problem was asked by Google.

# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree that consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_equal(s, t):
    # Case 1: both roots None
    if not s and not t:
        return True

    # Case 2: one root is None
    if (not s and t) or (s and not t):
        return False

    # Case 3: neither root is None
    return (s.val == t.val and
            is_equal(s.left, t.left) and
            is_equal(s.right, t.right))


def has_equal_subtree(s, t):
    if s is None:
        return not t

    if is_equal(s, t):
        return True

    return any([has_equal_subtree(s.left, t), has_equal_subtree(s.right, t)])


if __name__ == '__main__':
    TREE_1 = Node(1, Node(5, Node(6), Node(8)), Node(7))
    TREE_2 = Node(5, Node(6), Node(8))
    TREE_3 = Node(9)
    TREE_4 = Node(8)
    TREE_5 = Node(6, Node(1, Node(5, Node(6), Node(8)), Node(7)))
    TREE_6 = Node(5, Node(6), Node(9))

    print("Should be True: ", has_equal_subtree(TREE_1, TREE_2))
    print("Should be True: ", has_equal_subtree(TREE_1, TREE_4))
    print("Should be True: ", has_equal_subtree(TREE_5, TREE_1))
    print("Should be True: ", has_equal_subtree(TREE_5, TREE_2))
    print("Should be True: ", has_equal_subtree(TREE_5, TREE_4))

    print("Should be False: ", has_equal_subtree(TREE_2, TREE_1))
    print("Should be False: ", has_equal_subtree(TREE_1, TREE_3))
    print("Should be False: ", has_equal_subtree(TREE_1, TREE_3))
    print("Should be False: ", has_equal_subtree(TREE_5, TREE_6))
    print("Should be False: ", has_equal_subtree(TREE_2, TREE_5))


# Notes: This seems like the obvious way to do it, and it feels like there must
# be a better way, but that it will be complicated.

# Analysis: Actually this is pretty much exactly the first solution given.
# Merkle trees or string representations with a substring search are other
# options. The mismatching none case can be simplified to check if either is
# None.
