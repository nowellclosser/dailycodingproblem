# Find an efficient algorithm to find the smallest distance (measured in number
# of words) between any two given words in a string.

# For example, given words "hello", and "world" and a text content of
# "dog cat hello cat dog dog hello cat world", return 1 because there's only
# one word "cat" in between the two words.

import math
from collections import defaultdict


def smallest_word_distance(text, word_1, word_2):

    word_1_latest_index = None
    word_2_latest_index = None

    min_dist = math.inf

    for i, word in enumerate(text.split()):
        if word == word_1:
            word_1_latest_index = i
            if word_2_latest_index and i - word_2_latest_index < min_dist:
                min_dist = i - word_2_latest_index - 1

        if word == word_2:
            word_2_latest_index = i
            if word_1_latest_index and i - word_1_latest_index < min_dist:
                min_dist = i - word_1_latest_index - 1

    return min_dist


def preprocess(text):
    latest_index = {}
    min_pair_distances = defaultdict(lambda: math.inf)

    for i, word in enumerate(text.split()):
        for prev_word, idx in latest_index.items():
            if prev_word == word:
                continue

            key = "#".join(sorted([word, prev_word]))
            if i - idx - 1 < min_pair_distances[key]:
                min_pair_distances[key] = i - idx - 1

        latest_index[word] = i

    return min_pair_distances


if __name__ == '__main__':
    print(
        "Should be 1:",
        smallest_word_distance(
            "dog cat hello cat dog dog hello cat world",
            "hello",
            "world"
        )
    )

    print(
        "Should be 2:",
        smallest_word_distance(
            "dog cat hello cat dog dog hello cat world",
            "world",
            "dog"
        )
    )

    processed = preprocess("dog cat hello cat dog dog hello cat world")

    print("Should be 1:", processed["#".join(sorted(["hello", "world"]))])
    print("Should be 2:", processed["#".join(sorted(["world", "dog"]))])


# Notes: I expect they'll offer a preprocess solution as well.  In that case,
# you keep a dict of latest index by words seen, and then keep track of mins by
# pair in another dict, iterating over latest index keys and having a key
# delimited by # or something.  Then preprocess is O(n^2) but subsequent calls
# are constant time. Actually I'll just write that.

# There should be some handling of same-word queries to return 0 if present,
# and none otherwise probably.
