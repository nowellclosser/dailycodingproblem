# Given a list, sort it using this method: reverse(lst, i, j), which reverses
# lst from i to j


def reverse(lst, i, j):
    lst[i:j + 1] = lst[j:i - 1:-1]


def sort(lst):
    if len(lst) == 1:
        return

    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            continue

        insertion_point = 0
        for j in range(i - 1, -1, -1):
            if lst[j] <= lst[i]:
                insertion_point = j + 1
                break

        reverse(lst, insertion_point, i)
        reverse(lst, insertion_point + 1, i)


if __name__ == '__main__':
    x = [0, 1, 5, 2, 6, 7, 8, 9, 9, 4, 4, 4, 2]
    sort(x)
    print("Should be [0, 1, 2, 2, 4, 4, 4, 5, 6, 7, 8, 9, 9]: ", x)
