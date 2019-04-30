# This problem was asked by Google.

# Given the head of a singly linked list, swap every two nodes and return its
# head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


class Node():
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


def swap_pairs(node):

    head = node
    prev = None

    nxt = node.nxt
    while nxt:

        # Handle linking this pair to previous
        if not prev:
            head = nxt
        else:
            prev.nxt = nxt
        prev = node

        # Handle point node next at cur and cur at next next
        node.nxt = nxt.nxt
        nxt.nxt = node

        # Set up node and next for next iter
        node = node.nxt
        nxt = node.nxt if node.nxt else None

    return head


if __name__ == '__main__':
    NODE_1 = Node(1)
    NODE_2 = Node(2)
    NODE_3 = Node(3)
    NODE_4 = Node(4)
    NODE_5 = Node(5)

    NODE_1.nxt = NODE_2
    NODE_2.nxt = NODE_3
    NODE_3.nxt = NODE_4
    NODE_4.nxt = NODE_5

    new_head = swap_pairs(NODE_1)

    print("Should be 2 1 4 3 5 None: ",
          new_head.val, new_head.nxt.val,
          new_head.nxt.nxt.val, new_head.nxt.nxt.nxt.val,
          new_head.nxt.nxt.nxt.nxt.val, new_head.nxt.nxt.nxt.nxt.nxt)


# Analysis: Their solution is extremely concise, though this is fine.  Should
# maybe give theirs a closer look.  Yeah, they swap values, so you never mess
# with pointers, too.
