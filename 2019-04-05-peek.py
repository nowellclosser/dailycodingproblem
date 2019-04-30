# This problem was asked by Google.

# Given an iterator with methods next() and hasNext(), create a wrapper
# iterator, PeekableInterface, which also implements peek(). peek shows the
# next element that would be returned on next().

# Here is the interface:

# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass

#     def peek(self):
#         pass

#     def next(self):
#         pass

#     def hasNext(self):
#         pass


class PeekableInterface(object):
    def __init__(self, iterator):
        self._iterator = iterator

        self._stored_val = None
        self._val_stored = False
        self._done = False

    def peek(self):
        if self._val_stored:
            return self._stored_val

        try:
            self._stored_val = next(self._iterator)
            self._val_stored = True
        except(StopIteration):
            self._val_stored = False
            self._stored_val = None
            self._done = True

        return self._stored_val

    def next(self):
        if self._val_stored:
            self._val_stored = False
            return self._stored_val

        if self._done:
            raise StopIteration()

        return next(self._iterator)

    def has_next(self):
        self._peek()
        return self._done


if __name__ == '__main__':
    x = PeekableInterface(iter([1, 2, 3, 4]))
    print("Should be 1: ", x.next())
    print("Should be 2: ", x.next())
    print("Should be 3: ", x.peek())
    print("Should be 3: ", x.peek())
    print("Should be 3: ", x.next())
    print("Should be 4: ", x.next())
    print("Should be None: ", x.peek())

    print("Should print 'StopIteration raised':")
    try:
        x.next()
    except(StopIteration):
        print("StopIteration raised")


# Notes: I think it would make more sense to be overriding __next__ here.  Also
# peek returning None when it's over is sort of a bug- it should raise an
# exception or return an object that can specify when it's over, so that one
# can differentiate between there being no next element and the next element
# being None.
