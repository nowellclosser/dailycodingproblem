
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].

# Follow-up: what if you can't use division?

def product_of_others(numbers):
    product = numbers[0]
    for number in numbers[1:]:
        product *= number

    return [product // number for number in numbers]


def product_no_division(numbers):
    result = []
    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if not j == i:
                product *= numbers[j]
        result.append(product)

    return result

if __name__ == '__main__':
    print(product_of_others([1,2,3,4,5]))
    print(product_no_division([1,2,3,4,5]))
