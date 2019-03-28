# This problem was asked by Google.

# Given the root of a binary search tree, and a target K, return two nodes in
# the tree whose sum equals K.

# For example, given the following tree and K of 20

#     10
#    /   \
#  5      15
#        /  \
#      11    15
# Return the nodes 5 and 15.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_pair_exists(root, k):
    # Since DFS easier to implement than BFS, choose that. Since we don't need
    # recursion, avoid that.

    nums_needed = {k - root.val}
    node_stack = [root]

    while node_stack:
        node = node_stack.pop()

        if node.val in nums_needed:
            return True
        nums_needed.add(k - node.val)
        if node.left:
            node_stack.append(node.left)
        if node.right:
            node_stack.append(node.right)

    return False

if __name__ == '__main__':
    TREE_1 = Node(10, Node(5), Node(15, Node(11), Node(15)))
    print("Should be True:", sum_pair_exists(TREE_1, 20))
    print("Should be True:", sum_pair_exists(TREE_1, 30))
    print("Should be True:", sum_pair_exists(TREE_1, 26))
    print("Should be True:", sum_pair_exists(TREE_1, 16))
    print("Should be True:", sum_pair_exists(TREE_1, 21))
    print("Should be False:", sum_pair_exists(TREE_1, 23))
    print("Should be False:", sum_pair_exists(TREE_1, 230))
    print("Should be False:", sum_pair_exists(TREE_1, 10))
