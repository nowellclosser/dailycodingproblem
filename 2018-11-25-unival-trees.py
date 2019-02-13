# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def unival_count(root):
    unival_counter = 0

    def is_unival(root):
        if root is None:
            return True

        left_unival = is_unival(root.left)
        right_unival = is_unival(root.right)


        if (left_unival and right_unival and
                (getattr(root.left, 'val', None) == getattr(root.right, 'val', None)) and
                (root.left is None or (root.left.val == root.val))):
            nonlocal unival_counter
            unival_counter += 1
            return True

        return False

    is_unival(root)

    return unival_counter


if __name__ == '__main__':
    node = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(unival_count(node))
