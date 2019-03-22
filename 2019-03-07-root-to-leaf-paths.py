# This problem was asked by Facebook.

# Given a binary tree, return all paths from the root to leaves.

# For example, given the tree:

#    1
#   / \
#  2   3
#     / \
#    4   5
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_leaf_paths(tree):
    paths = []

    def helper(node, cur_path=[]):
        cur_path = cur_path + [node.val]
        nonlocal paths

        if not node.left and not node.right:
            paths.append(cur_path)
            return

        if node.left:
            helper(node.left, cur_path)
        if node.right:
            helper(node.right, cur_path)

    helper(tree)
    return paths

if __name__ == '__main__':
    TREE_1 = Node(1, Node(2), Node(3, Node(4), Node(5)))
    print("Shd be [[1, 2], [1, 3, 4], [1, 3, 5]]: ", root_leaf_paths(TREE_1))


# Notes: quite easy, especially with the nonlocal. Took maybe 15 min including
# testing.

# Analysis: They didn't use recursion, which is not too complicated here,
# though their solution seems convoluted, modifying the node class to print a
# given node's path.  Mine prebuild paths and rattles them off once you get to
# a leaf, whereas they find all leaves, iterate through, and run their path
# building function.

# Interesting point that avoiding recursion on a large or unknown tree is a
# a good tactic, though.  Yeah, good use of iterative DFS.
