# Using a read7() method that returns 7 characters from a file, implement
# readN(n) which reads n characters.

# For example, given a file with the content “Hello world”, three read7()
# returns “Hello w”, “orld” and then “”.


def read7(open_file):
    return open_file.read(7)


def readn(n, filename):
    result = ""
    with open(filename) as f:
        while n > 7:
            result += read7(f)
            n -= 7

        result += read7(f)[:n]

    return result


if __name__ == '__main__':

    with open("sample_file_1.txt") as f:
        print("Should be 'Here ar': '{}'".format(read7(f)))
        print("Should be 'Here ar': '{}'".format(read7(f)))

    print("Should be 'Here are a bunch of characters': '{}'".format(
        readn(30, "sample_file_1.txt"))
    )

# Notes:
# 4 minutes in read7 is good to go. Started clock at first draft.

# 16 minutes in. Not really. Not sure if it is supposed to save its state
# somehow or not. Pausing.

# Ok made it take an open file handle at 20 min, so that state can be "saved".

# All good at 30 min.

# Analysis:
# Don't really understand their solution, to be honest.  I think mine is better
# and that this question is not super well-posed.
