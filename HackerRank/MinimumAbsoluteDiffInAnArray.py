import sys


def minimumAbsoluteDifference(arr):
    arr = sorted(list(map(int, arr)))
    min_diff = sys.maxsize

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == '__main__':
    import large_input_helper

    test_arr, expected = large_input_helper.min_abs_diff_arr()

    test_answer = minimumAbsoluteDifference(test_arr)

    print(test_answer == expected)
