# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def sum_pair_exists(numbers, desired_sum):
    values_needed = set()

    for num in numbers:
        if num in values_needed:
            return True
        values_needed.add(desired_sum - num)

    return False

if __name__ == '__main__':
    LIST = [10, 15, 3, 7, -1, 0]
    print(LIST)
    print("Desired sum:")
    print(sum_pair_exists(LIST, int(input())))

