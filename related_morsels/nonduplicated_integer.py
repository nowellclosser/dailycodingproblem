def non_dup(num_list):
    result_array = [0] * 32

    for num in num_list:
        remainder = num
        for i in range(len(result_array)):
            bit = num >> (32 - i - 1)
            remainder = remainder - bit << (32 - i - 1)
            result_array[i] = (result_array[i] + bit) % 2

    return sum([b * 2 ** (32 - i - 1) for i, b in enumerate(result_array)])

if __name__ == '__main__':
    print(non_dup([1, 2, 3, 1, 2, 5, 3, 7, 5, 7, 7, 7, 5]))
