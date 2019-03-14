# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.

from collections import deque


class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach: BFS, keeping track of level sums. We will call level 1 the root
# node.
def max_sum_level(node):
    if not node:
        return None

    q = deque()
    q.append(node)

    level = 1
    level_sum = node.val

    max_level = level
    max_level_sum = level_sum

    while q:
        level_sum = 0

        level_size = len(q)
        while level_size:
            node = q.popleft()
            level_sum += node.val
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
            level_size -= 1

        if level_sum > max_level_sum:
            max_level = level
            max_level_sum = level_sum

        level += 1

    return max_level

if __name__ == '__main__':
    TREE_1 = Node(1, Node(-1, right=Node(5)), Node(2, Node(-7)))
    print("Should be 1:", max_sum_level(TREE_1))

    TREE_2 = Node(1, Node(-1, right=Node(5)), Node(2, Node(7)))
    print("Should be 3:", max_sum_level(TREE_2))

    TREE_3 = Node(1, Node(1, Node(-10), Node(5)), Node(2, Node(7)))
    print("Should be 2:", max_sum_level(TREE_3))
