# Given a list of words, find all pairs of unique indices such that the
# concatenation of the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return
# [(0, 1), (1, 0), (2, 3)].


def is_palindrome_pair(left, right):

    l = 0
    r = len(right) - 1

    while l < len(left) and r >= 0:
        if left[l] != right[r]:
            return False
        l += 1
        r -= 1

    return True


def palindrome_pairs(words):

    pairs = []
    for i, right in enumerate(words):
        for j, left in enumerate(words[:i]):
            if is_palindrome_pair(left, right):
                pairs.append((j, i))
                if len(left) == len(right):
                    pairs.append((i, j))
                    continue
            if is_palindrome_pair(right, left):
                pairs.append((i, j))

    return pairs


if __name__ == '__main__':
    print("Should be [(0, 1), (1, 0), (2, 3)]: ",
          palindrome_pairs(["code", "edoc", "da", "d"]))


# Notes: This isn't a great improvement over brute force, but it seems to me
# you CAN'T improve over brute force very much:  You have to process n(n-1)/2
# = O(n^2) pairs regardless, and the improvements must come in how you deal
# the inverse of each pair.  The same length shortcut is simple enough, but no
# other shortcuts were apparent to me that would be quicker than iterating
# through.  Even though, these shortcuts are affecting the constant factor
# on the runtime.
