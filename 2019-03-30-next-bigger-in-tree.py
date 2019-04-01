# This problem was asked by Amazon.

# Given a node in a binary search tree, return the next bigger element,
# also known as the inorder successor.

# For example, the inorder successor of 22 is 30.

#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.

from math import inf


class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def next_larger(node):
    next_largest_node = None

    # Stack of (node, preceding node)
    stack = [(node, None)]
    while stack:
        cur, prev = stack.pop()
        for next_node in [cur.left, cur.right, cur.parent]:
            if next_node != prev and next_node:
                stack.append((next_node, cur))

        if (node.val < cur.val <
                (next_largest_node.val if next_largest_node else inf)):
            next_largest_node = cur

    return next_largest_node

if __name__ == '__main__':
    node_1 = Node(10)
    node_2 = Node(5)
    node_3 = Node(30)
    node_4 = Node(22)
    node_5 = Node(35)

    node_1.left = node_2
    node_1.right = node_3
    node_2.parent = node_1
    node_3.parent = node_1
    node_3.left = node_4
    node_3.right = node_5
    node_4.parent = node_3
    node_5.parent = node_3

    print("Should be 30:", next_larger(node_4).val)
    print("Should be 35:", next_larger(node_3).val)
    print("Should be 22:", next_larger(node_1).val)
    print("Should be None:", next_larger(node_5))


# Notes: This is basically just a rotated traversal problem. I started to do
# it recursively and it was much more complex, so I just scrapped it and did
# an iterative DFS.

# Analysis: I forgot the full definition of binary search tree, which imposes
# some additional structure here: ALL nodes in left tree of a node must be less
# than it, and ALL nodes in right tree must be greater.

# In that case, the answer is either the leftmost descendant of the right child
# or, if none, the first parent going up parents that had a left child in the
# chain.
