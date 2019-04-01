# This problem was asked by Facebook.

# You have a large array with most of the elements as zero.

# Use a more space-efficient data structure, SparseArray, that implements the
# same interface:

# init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.

from collections import defaultdict

import unittest


class SparseArray():
    def __init__(self, arr):
        self.entries = defaultdict(int)
        self.len = len(arr)
        for i, val in enumerate(arr):
            if val:
                self.entries[i] = val

    def set(self, i, val):
        if i < 0 or i >= self.len:
            raise IndexError()

        self.entries[i] = val

    def get(self, i):
        if i < 0 or i >= self.len:
            raise IndexError()

        return self.entries[i]


class TestSparseArray(unittest.TestCase):
    def test_get_and_set(self):
        example = SparseArray([1, 0, 0, 6, 0, 0, 1, 1, 11, 0, 0])

        self.assertEqual(example.get(0), 1)
        self.assertEqual(example.get(1), 0)
        self.assertEqual(example.get(3), 6)
        self.assertEqual(example.get(8), 11)

        example.set(2, 10)
        self.assertEqual(example.get(2), 10)

        example.set(3, 18)
        self.assertEqual(example.get(3), 18)

    def test_out_of_range(self):
        example = SparseArray([1, 0, 0, 6, 0, 0, 1, 1, 11, 0, 0])

        with self.assertRaises(IndexError):
            example.get(20)

        with self.assertRaises(IndexError):
            example.set(20, 20)


if __name__ == '__main__':
    unittest.main()


# Analysis: Easy. One thing they did which I missed is to clean up an entry if
# it's set to 0, but otherwise our solutions are very similar.  And extracting
# the bound-checking so it's not duplicated was an improvement relative to
# mine.
