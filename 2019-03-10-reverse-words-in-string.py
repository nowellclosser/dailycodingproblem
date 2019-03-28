# This problem was asked by Google.

# Given a string of words delimited by spaces, reverse the words in string. For
# example, given "hello world here", return "here world hello"

# Follow-up: given a mutable string representation, can you perform this
# operation in-place?


# This would be the mutable if we wrote in-place reverse.
# Barring that, we can simply reverse the list of tokens
def reverse_words(string):
    return ' '.join([token[::-1] for token in string.split(' ')])[::-1]

if __name__ == '__main__':
    print("Should be here world hello: ", reverse_words("hello word here"))


# Analysis: My solution is kind of silly as is- either just use reversed() or
# actually write the reverse functionality that *would* do it in-place instead
# of doing [::-1].  But I understand both ways and was just a bit lazy
# implementing this.
