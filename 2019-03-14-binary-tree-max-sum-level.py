# This problem was asked by Facebook.

# Given a binary tree, return the level of the tree with minimum sum.

class Node():
    def __init__(val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_sum_level(node):

