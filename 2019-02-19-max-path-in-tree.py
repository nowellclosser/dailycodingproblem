# This problem was asked by Google.

# Given a binary tree of integers, find the maximum path sum between two nodes.
# The path must go through at least one node, and does not need to go through
# the root.


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_sum(node):
    def helper(node):
        if not node:
            return (float("-inf"), 0)

        left_max, left_path = helper(node.left)
        right_max, right_path = helper(node.right)

        max_through_node = max(left_path, 0) + node.val + max(right_path, 0)
        total_max = max(left_max, max_through_node, right_max)
        max_ending_at_node = max(left_path, right_path, 0) + node.val

        return (total_max, max_ending_at_node)

    return helper(node)[0]

if __name__ == '__main__':
    TREE_1 = Node(9, Node(5), Node(6))
    print("Should be 20: ", max_sum(TREE_1))

    TREE_2 = Node(9, Node(-1, Node(50), Node(40)), Node(6))
    #         9
    #     -1      6
    # 50      40
    print("Should be 89: ", max_sum(TREE_2))

    TREE_3 = Node(-10, Node(20, Node(15), Node(7)), Node(9))
    #         9
    #     -1      6
    # 50      40
    print("Should be 42: ", max_sum(TREE_3))


# Notes: The definition of path is unclear to me here, still.
# This is simply an implementation of the solution after loooking at it for
# practice.
