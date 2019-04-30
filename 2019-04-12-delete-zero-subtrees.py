# This question was asked by BufferBox.

# Given a binary tree where all nodes are either 0 or 1, prune the tree so that
# subtrees containing all 0s are removed.

# For example, given the following tree:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0
# should be pruned to:

#    0
#   / \
#  1   0
#     /
#    1
# We do not remove the tree at the root or its left child because it still has
# a 1 as a descendant.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_all_zero(node):
    if not node:
        return True
    return (node.val == 0 and is_all_zero(node.left) and
            is_all_zero(node.right))


def prune_zero_trees(node):

    def prune_helper(node):
        if not node:
            return

        if is_all_zero(node.left):
            node.left = None

        if is_all_zero(node.right):
            node.right = None

    if not node or is_all_zero(node):
        return None

    if is_all_zero(node.left):
        node.left = None

    if is_all_zero(node.right):
        node.right = None

    prune_helper(node.left)
    prune_helper(node.right)

    return node


if __name__ == '__main__':
    TREE_1 = Node(1, Node(5), Node(0, Node(0), Node(0)))
    TREE_2 = Node(1, Node(5), Node(0, Node(0), Node(1)))
    TREE_3 = Node(0, Node(0), Node(0, Node(0), Node(0)))

    PRUNED_TREE_1 = prune_zero_trees(TREE_1)
    PRUNED_TREE_2 = prune_zero_trees(TREE_2)
    PRUNED_TREE_3 = prune_zero_trees(TREE_3)

    print("Should be 5 None:", PRUNED_TREE_1.left.val, PRUNED_TREE_1.right)
    print("Should be 5 None 1:", PRUNED_TREE_2.left.val,
          PRUNED_TREE_2.right.left, PRUNED_TREE_2.right.right.val)
    print("Should be None:", PRUNED_TREE_3)


# Notes: that this both modifies the tree and returns a tree is confusing,
# and simply the way I handled the case of a fully pruned tree.  Maybe it would
# have been better to never modify the tree.

# Analysis- The recursion can be simplified- should maybe do again. It's the
# same thing, but cleaner.
