# Given a tree, find the largest tree/subtree that is a BST.

# Given a tree, return the size of the largest tree/subtree that is a BST.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_bst(node, max_val=None, min_val=None):

    val_ok = True

    if min_val and node.val < min_val:
        val_ok = False
    if max_val and node.val > max_val:
        val_ok = False

    left_ok = not node.left or (
        node.left.val <= node.val and is_bst(node.left, node.val, min_val)
    )
    right_ok = not node.right or (
        node.val <= node.right.val and is_bst(node.right, max_val, node.val)
    )
    return val_ok and left_ok and right_ok


def size(node):
    if not node:
        return 0

    return 1 + size(node.left) + size(node.right)


def find_largest_bst(node):
    if not node:
        return 0
    if is_bst(node):
        return size(node)

    return max(find_largest_bst(node.left), find_largest_bst(node.right))

if __name__ == '__main__':
    TREE_1 = Node(1, Node(5), Node(6))
    print("Should be 1: ", find_largest_bst(TREE_1))

    TREE_2 = Node(3, Node(1, Node(5), Node(6)), Node(5))
    print("Should be 1: ", find_largest_bst(TREE_2))

    TREE_3 = Node(5, Node(5, Node(4, Node(3), Node(6)), Node(7)),
                  Node(9, Node(9), Node(9)))
#                5
#            /       \
#        5            9
#      /   \         / \
#    4      7       9   9
#  /   \
# 3     6
    print("Should be 3: ", find_largest_bst(TREE_3))

    TREE_4 = Node(6, Node(1), Node(6))
    print("Should be 3: ", find_largest_bst(TREE_4))

    TREE_5 = Node(5, Node(4, Node(3), Node(4)), Node(6, Node(6),
                  Node(9, Node(7), Node(10))))

#                5
#            /       \
#        4            6
#      /   \         / \
#    3      4       6   9
#                      / \
#                     7   10
    print("Should be 9: ", find_largest_bst(TREE_5))

# Notes: While I'm happy with this solution, I realized it only allows
# subtrees ending on leaves, which I don't think is the intention.  Nvm,
# subtree is any node and all its descendants, so this is good.

# Analysis: Size and bst check can be combined to make this O(N) instead of
# O(N^2) in worst case.  Uses nonlocals and helper!
