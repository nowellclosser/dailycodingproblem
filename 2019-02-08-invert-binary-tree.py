# This problem was asked by Google.

# Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(node):
    if node:
        node.left, node.right = invert_tree(node.right), invert_tree(node.left)
        return node

if __name__ == '__main__':
    TREE = Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f")))
    print("Should be f", TREE.right.left.val)
    print("Should be d", TREE.left.left.val)
    print("Should be e", TREE.left.right.val)
    print("Should be b", TREE.left.val)
    print("Should be c", TREE.right.val)
    invert_tree(TREE)
    print("Should be e", TREE.right.left.val)
    print("Should be f", TREE.left.right.val)
    print("Should be d", TREE.right.right.val)
    print("Should be c", TREE.left.val)
    print("Should be b", TREE.right.val)
