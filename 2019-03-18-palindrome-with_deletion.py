# This problem was asked by Google.

# Given a string which we can delete at most k, return whether you can make a
# palindrome.

# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to
# get 'waterretaw'.


def can_make_palindrome(string, max_deletions):
    if max_deletions < 0:
        return False

    if len(string) <= max(1, max_deletions):
        return True

    if string[0] == string[len(string) - 1]:
        if can_make_palindrome(string[1:-1], max_deletions):
            return True

    return (can_make_palindrome(string[1:], max_deletions - 1) or
            can_make_palindrome(string[:-1], max_deletions - 1))

if __name__ == '__main__':
    print('Should be True: ', can_make_palindrome('waterrfetawx', 2))
    print('Should be True: ', can_make_palindrome('waterrfetawxaw', 4))
    print('Should be False: ', can_make_palindrome('waterrfetawx', 1))
    print('Should be True: ', can_make_palindrome('wasdfghjklqeryuiow', 20))
    print('Should be True: ', can_make_palindrome('racecar', 0))
    print('Should be True: ', can_make_palindrome('raccar', 0))
    print('Should be True: ', can_make_palindrome('xraccar', 1))
    print('Should be False: ', can_make_palindrome('xraccar', 0))


# Analysis: This is one solution given, exponentialish in the worst case.  They
# also used a while loop to remove outer matches, but didn't early out based on
# string size compared to max deletions.

# In any case, for large n and k there is a dynamic programming approach that
# is better- find the largest palindromic subsequence in O(n^2) time and
# compare to len - k.
