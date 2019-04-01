# This question was asked by Snapchat.

# Given the head to a singly linked list, where each node also has a “random”
# pointer that points to anywhere in the linked list, deep clone the list.


class Node():
    def __init__(self, val, nxt=None, rand=None):
        self.val = val
        self.nxt = nxt
        self.rand = rand


def deep_clone(ll):
    index_map = {}

    src = ll
    cpy = [Node(ll.val)]
    rand_nodes = [ll.rand]

    idx = 0

    index_map[src] = idx

    while src.nxt:
        src = src.nxt

        cpy.append(Node(src.val))
        cpy[-2].nxt = cpy[-1]

        rand_nodes.append(src.rand)

        idx += 1
        index_map[src] = idx

    for i, rand_node in enumerate(rand_nodes):
        cpy[i].rand = cpy[index_map[rand_node]]

    return cpy[0]

if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(4)
    node3 = Node(6)
    node4 = Node(-4)

    node1.nxt = node2
    node2.nxt = node3
    node3.nxt = node4

    node1.rand = node1
    node2.rand = node1
    node3.rand = node4
    node4.rand = node2

    cpy = deep_clone(node1)
    print("Should be 3 4 6 -4 None 3 3 -4 4: ",
          cpy.val, cpy.nxt.val, cpy.nxt.nxt.val, cpy.nxt.nxt.nxt.val,
          cpy.nxt.nxt.nxt.nxt,
          cpy.rand.val, cpy.nxt.rand.val, cpy.nxt.nxt.rand.val,
          cpy.nxt.nxt.nxt.rand.val)

    print("Should be different:", cpy.nxt, node1.nxt)
    print("Should be different:", cpy.nxt.rand, node1.nxt.rand)
