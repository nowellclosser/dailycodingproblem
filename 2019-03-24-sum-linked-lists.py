# This problem was asked by Microsoft.

# Let's represent an integer in a linked list format by having each node
# represent a digit in the number. The nodes make up the number in reversed
# order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked
# list format.

# For example, given

# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:

# 4 -> 2 -> 1


class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def sum_lls(l, r):
    carry = False
    last_node = None
    head = None

    while l or r:
        # Find digit in current place and whether to carry
        val = (l.val if l else 0) + (r.val if r else 0) + carry
        if val >= 10:
            val = val % 10
            carry = True
        else:
            carry = False

        # Build node with that value and either link to previous node or
        # establish as head
        new_node = Node(val)
        if last_node:
            last_node.next = new_node
        else:
            head = new_node
        last_node = new_node

        # Advance in each list if possible
        if l:
            l = l.next
        if r:
            r = r.next

    if carry:
        last_node.next = Node(1)

    return head

if __name__ == '__main__':
    _99 = Node(9, Node(9))
    _25 = Node(5, Node(2))

    _sum = sum_lls(_99, _25)
    print("Should be 4 2 1 None: ",
          _sum.val, _sum.next.val, _sum.next.next.val, _sum.next.next.next)

    _sum = sum_lls(_25, _99)
    print("Should be 4 2 1 None: ",
          _sum.val, _sum.next.val, _sum.next.next.val, _sum.next.next.next)


# Notes: don't really gain that much by implementing the addition algorithm,
# but did it for fun.

# Analysis: Actually implementing addition appears to be what they intended.
# They did it recursively but I like this well enough.
