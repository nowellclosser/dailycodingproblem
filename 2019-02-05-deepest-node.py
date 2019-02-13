# This problem was asked by Google.

# Given the root of a binary tree, return a deepest node. For example, in the
# following tree, return d.

#     a
#    / \
#   b   c
#  /
# d


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deepest_node(node):

    if not node:
        return None
    max_depth = 1
    deepest_node = node

    def recursive_helper(node, depth):

        nonlocal deepest_node
        nonlocal max_depth

        if not node.left and not node.right:
            if depth > max_depth:
                deepest_node = node
                max_depth = depth
            return

        for node in node.left, node.right:
            if node:
                recursive_helper(node, depth + 1)

    for node in node.left, node.right:
        if node:
            recursive_helper(node, 1)

    return deepest_node.val

if __name__ == '__main__':
    TREE = Node("a", Node("b", Node("d")), Node("c"))
    print("Should be d: ", deepest_node(TREE))


# Notes: This took probably 20 mins. The nonlocal + helper pattern really
# makes these simple, but lacks the purity of the single recursive function.

# Analysis: The real solution is nice conceptually. I should write more of
# these # like that as an exercise.
