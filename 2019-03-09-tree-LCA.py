# This problem was asked by Twitter.

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree. Assume that each node in the tree also has a pointer to its
# parent.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”


class Node():
    def __init__(self, val, parent=None):
        self.val = val
        self.parent = parent


def lca(node_1, node_2):
    if node_1 == node_2:
        return node_1

    node_1_ancestors = set()
    node_1_ancestors.add(node_1)

    while node_1.parent:
        if node_1.parent == node_2:
            return node_2
        node_1_ancestors.add(node_1.parent)
        node_1 = node_1.parent

    while node_2.parent:
        if node_2.parent in node_1_ancestors:
            return node_2.parent
        node_2 = node_2.parent

    raise Exception("Tree must be malformed! No common ancestor found")

if __name__ == '__main__':
    root = Node(0)
    child_1 = Node(1, root)
    child_2 = Node(2, root)
    child_3 = Node(3, child_1)
    child_4 = Node(4, child_1)
    child_5 = Node(5, child_2)
    child_6 = Node(6, child_2)
    child_7 = Node(7, child_6)

#                 0
#              1    2
#            3   4 5  6
#                       7

    print("Should be 0", lca(child_7, child_4).val)
    print("Should be 0", lca(child_6, child_4).val)
    print("Should be 0", lca(child_7, child_3).val)
    print("Should be 0", lca(child_3, child_7).val)
    print("Should be 0", lca(child_7, child_1).val)
    print("Should be 2", lca(child_7, child_5).val)
    print("Should be 7", lca(child_7, child_7).val)
    print("Should be 6", lca(child_7, child_6).val)
    print("Should be 6", lca(child_6, child_7).val)
    print("Should be 1", lca(child_3, child_4).val)
    print("Should be 1", lca(child_4, child_3).val)
