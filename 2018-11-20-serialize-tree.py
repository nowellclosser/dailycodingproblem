# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string
# back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

import json

def serialize(root):
    if root is None:
        return 'null'
    return '["{}",{},{}]'.format(
        root.val, serialize(root.left), serialize(root.right)
    )

def deserialize(tree_string):
    return deserialize_node_list(json.loads(tree_string))

def deserialize_node_list(node_list):
    if node_list is None:
        return None
    return Node(
        node_list[0],
        deserialize_node_list(node_list[1]),
        deserialize_node_list(node_list[2]),
    )

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    print(deserialize(serialize(node)).left.left.val)
    assert deserialize(serialize(node)).left.left.val == 'left.left'
