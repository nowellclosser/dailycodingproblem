# This problem was asked by Microsoft.

# Implement 3 stacks using a single list:

# class Stack:
#     def __init__(self):
#         self.list = []

#     def pop(self, stack_number):
#         pass

#     def push(self, item, stack_number):
#         pass

import unittest


class Stack:
    def __init__(self):
        self.list = []
        self.ends = [0, 0]

    def pop(self, stack_number):
        if stack_number < 0 or stack_number > 2:
            raise Exception("Invalid stack number")

        if stack_number == 2:
            if self.ends[1] >= len(self.list):
                raise IndexError("pop from empty list")
            result = self.list.pop()

        else:
            if ((stack_number == 0 and self.ends[0] == 0) or
                    (stack_number == 1 and self.ends[1] == self.ends[0])):
                raise IndexError("pop from empty list")

            result = self.list.pop(self.ends[stack_number] - 1)
            for i in range(stack_number, 2):
                self.ends[i] -= 1

        return result

    def push(self, item, stack_number):
        if stack_number < 0 or stack_number > 2:
            raise Exception("Invalid stack number")

        if stack_number == 2:
            self.list.append(item)

        else:
            self.list.insert(self.ends[stack_number], item)
            for i in range(stack_number, 2):
                self.ends[i] += 1


class TestStack(unittest.TestCase):
    def test_empty(self):
        x = Stack()
        with self.assertRaises(IndexError):
            x.pop(2)

        with self.assertRaises(IndexError):
            x.pop(1)

        with self.assertRaises(IndexError):
            x.pop(0)

    def test_nonempty(self):
        x = Stack()

        x.push(3, 2)
        # ||3
        # 0,0
        x.push(2, 1)
        # |2|3
        # 0,1
        x.push(1, 0)
        # 1|2|3
        # 1,2
        x.push(5, 1)
        # 1|2,5|3
        # 1,3
        x.push(4, 2)
        # 1|2,5|3,4
        # 1,3
        x.push(6, 0)
        # 1,6|2,5|3,4
        # 2,4

        self.assertEqual(x.pop(1), 5)
        self.assertEqual(x.pop(1), 2)
        self.assertEqual(x.pop(0), 6)
        self.assertEqual(x.pop(0), 1)
        self.assertEqual(x.pop(2), 4)
        self.assertEqual(x.pop(2), 3)

        with self.assertRaises(IndexError):
            x.pop(2)

        with self.assertRaises(IndexError):
            x.pop(1)

        with self.assertRaises(IndexError):
            x.pop(0)

if __name__ == '__main__':
    unittest.main()


# Notes: more tedious than it seems. I was a little slow.
