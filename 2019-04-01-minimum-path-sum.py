# This question was asked by Apple.

# Given a binary tree, find a minimum path sum from root to a leaf.

# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum
# 15.

#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimum_complete_path_sum(node):
    if not node:
        return 0
    return node.val + min(minimum_complete_path_sum(node.left),
                          minimum_complete_path_sum(node.right))

if __name__ == '__main__':
    TREE_1 = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))

    print("Should be 15:", minimum_complete_path_sum(TREE_1))

# Analysis: this is fine- they have a typo and wanted the minimum sum path,
# which is a tiny bit harder, but pretty simple.
