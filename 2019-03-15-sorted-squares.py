# This problem was asked by Google.

# Given a sorted list of integers, square the elements and give the output in
# sorted order.

# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


def sorted_squares(sorted_list):

    neg_squares = []
    nonneg_squares = []
    for element in sorted_list:
        if element < 0:
            neg_squares.append(element ** 2)
        else:
            nonneg_squares.append(element ** 2)

    return merge(neg_squares[::-1], nonneg_squares)


def merge(l, r):
    merged_list = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(l) or r_idx < len(r):
        left_element = l[l_idx] if l_idx < len(l) else None
        right_element = r[r_idx] if r_idx < len(r) else None

        if left_element is None or (right_element is not None and
                                    right_element < left_element):
            merged_list.append(right_element)
            r_idx += 1

        else:
            merged_list.append(left_element)
            l_idx += 1

    return merged_list

if __name__ == '__main__':
    print("Should be [0, 4, 4, 9, 81]: ", sorted_squares([-9, -2, 0, 2, 3]))
