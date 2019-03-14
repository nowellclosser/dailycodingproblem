# This problem was asked by LinkedIn.

# Determine whether a tree is a valid binary search tree.

# A binary search tree is a tree with two children, left and right, and
# satisfies the constraint that the key in the left child must be less than
# or equal to the root and the key in the right child must be greater than or
# equal to the root.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_binary_search_tree(node):
    if not node:
        return True
    left_val_ok = node.left is None or node.left.val <= node.val
    right_val_ok = node.right is None or node.right.val >= node.val

    return (left_val_ok and right_val_ok and
            is_binary_search_tree(node.left) and
            is_binary_search_tree(node.right))


def is_binary_search_tree_redo(node, prev_mx=None, prev_mn=None):
    if not node:
        return True

    print(node.val, prev_mx, prev_mn)

    if (prev_mn and not prev_mn <= node.val or
            prev_mx and not prev_mx >= node.val):
        return False

    return (is_binary_search_tree_redo(node.left, node.val, prev_mn) and
            is_binary_search_tree_redo(node.right, prev_mx, node.val))


if __name__ == '__main__':
    BAD_TREE_1 = Node(1, Node(5), Node(6))
    print("Should be False: ", is_binary_search_tree_redo(BAD_TREE_1))

    BAD_TREE_2 = Node(3, Node(1, Node(5), Node(6)), Node(5))
    print("Should be False: ", is_binary_search_tree_redo(BAD_TREE_2))

    BAD_TREE_3 = Node(5, Node(5, Node(4, Node(3), Node(6)), Node(7)),
                      Node(9, Node(9), Node(9)))
#                5
#            /       \
#        5            9
#      /   \         / \
#    4      7       9   9
#  /   \
# 3     6  7
    print("Should be False: ", is_binary_search_tree_redo(BAD_TREE_3))

    GOOD_TREE_1 = Node(6, Node(1), Node(6))
    print("Should be True: ", is_binary_search_tree_redo(GOOD_TREE_1))

    GOOD_TREE_2 = Node(5, Node(4, Node(3), Node(4)), Node(6, Node(6),
                       Node(9, Node(7), Node(10))))

#                5
#            /       \
#        4            6
#      /   \         / \
#    3      4       6   9
#                      / \
#                     7   10
    print("Should be True: ", is_binary_search_tree_redo(GOOD_TREE_2))

# Notes: Did swiftly, ran and passed tests on first try, which is pretty
# sweet.

# Ahh. Another poorly worded problem description.  All the keys in the left and
# right subtrees must be less than the root.  Will redo later.

# Analysis on redo: Not super smooth, but got it in a moderate amount of time.
