# This problem was asked by Facebook.

# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given
# "hello/world:here", return "here/world:hello"

# Follow-up: Does your solution work for the following cases:
# "hello/world:here/", "hello//world:here"


def _reverse(string):
    words = []
    chars = []

    delimiters = []

    for char in string:
        if char.isalnum():
            chars.append(char)
        else:
            delimiters.append(char)
            words.append(''.join(chars or []))
            chars = []

    words.append(''.join(chars or []))

    result = []

    d_idx = 0
    for word in words[::-1]:
        result.append(word)
        if d_idx < len(delimiters):
            result.append(delimiters[d_idx])
        d_idx += 1

    return ''.join(result)

if __name__ == '__main__':
    print("Should be 'here/world:hello': ", _reverse("hello/world:here"))
    print("Should be '/here:world/hello': ", _reverse("hello/world:here/"))
    print("Should be 'here/world/:hello': ", _reverse("hello//world:here"))
