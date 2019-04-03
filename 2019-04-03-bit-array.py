# This problem was asked by Amazon.

# Implement a bit array.

# A bit array is a space efficient array that holds a value of 1 or 0 at each
# index.

# init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.

from collections import defaultdict
import unittest


class BitArray():
    def __init__(self, size):
        self.size = size
        self.store = defaultdict(lambda: False)

    def _check_bounds(self, i):
        if i < 0 or i >= self.size:
            raise IndexError()

    def set(self, i, val):
        self._check_bounds(i)
        if val:
            self.store[i] = val
        else:
            del self.store[i]

    def get(self, i):
        self._check_bounds(i)
        return int(self.store[i])


class TestBitArray(unittest.TestCase):
    def test_get_and_set(self):
        example = BitArray(20)

        self.assertFalse(example.get(0))
        self.assertFalse(example.get(19))

        example.set(2, 1)
        self.assertEqual(example.get(2), 1)

        example.set(2, 0)
        self.assertEqual(example.get(2), 0)

    def test_out_of_range(self):
        example = BitArray(20)

        with self.assertRaises(IndexError):
            example.get(20)

        with self.assertRaises(IndexError):
            example.set(20, 1)

if __name__ == '__main__':
    unittest.main()
