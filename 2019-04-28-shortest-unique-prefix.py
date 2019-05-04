# This problem was asked by Square.

# Given a list of words, return the shortest unique prefix of each word.
# For example, given the list:

# dog
# cat
# apple
# apricot
# fish
# Return the list:

# d
# c
# app
# apr
# f


class Trie:
    def __init__(self):
        self.state = {}

    def add(self, word):
        level_dict = self.state
        for letter in word:
            if letter not in level_dict:
                level_dict[letter] = {}
            level_dict = level_dict[letter]

    def shortest_unique_prefix(self, word):
        level_dict = self.state
        highest_branch = -1
        for i, letter in enumerate(word):
            if len(level_dict[letter]) > 1:
                highest_branch = i

            level_dict = level_dict[letter]

        if highest_branch == len(word) - 1:
            return None

        return word[:highest_branch + 2]


def shortest_unique_prefixes(words):
    trie = Trie()

    for word in words:
        trie.add(word)

    result = []
    for word in words:
        result.append(trie.shortest_unique_prefix(word))

    return result


if __name__ == '__main__':
    WORDS = ['dog', 'cat', 'apple', 'apricot', 'fish']
    print("Should be [d, c, app, apr, f]:",
          shortest_unique_prefixes(WORDS))


# Notes: This is kind of ugly.  I think I should actually have implemented
# a trie without dicts, so that I could have multiple copies of the same child,
# and would know immediately when I'm at the shortest prefix.

# Analysis: yeah they did this with a real multi child node implementation.
# Otherwise similar.
