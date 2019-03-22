# This problem was asked by Google.

# Given a word W and a string S, find all starting indices in S which are
# anagrams of W.

# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

from collections import defaultdict


def anagram_indices(string, word):
    word_set = set(word)

    index_status_map = defaultdict(set)
    complete_indices = []

    for i, char in enumerate(string):
        for index, letters_needed in index_status_map.copy().items():
            if char in letters_needed:
                letters_needed.remove(char)
                if not letters_needed:
                    del index_status_map[index]
                    complete_indices.append(index)
            else:
                del index_status_map[index]
        if char in word_set:
            index_status_map[i] = word_set - set(char)

    return complete_indices

if __name__ == '__main__':
    print("Should be [0, 3, 4]: ", anagram_indices("abxaba", "ab"))
    print("Should be [0, 2, 3, 4, 5, 11]: ",
          anagram_indices("abcbacbadababcx", "abc"))
    print("Should be []: ", anagram_indices("abxaba", "abc"))


# Analysis: I think I prefer this to the provided solution, which loops through
# the string twice, whereas this just loops through once and checks some sets
# potentially.
