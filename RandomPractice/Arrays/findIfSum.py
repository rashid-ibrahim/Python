"""
Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the
given value.
"""


def find_integers_of_sum(arr, sum):
    # For brevity I am just using the built in sort instead of rolling a sort algorithm
    arr.sort()

    l, r = 0, len(arr)-1

    while l < r:
        current = arr[l] + arr[r]
        if current == sum:
            return arr[l], arr[r]
        elif current < sum:
            l += 1
        elif current > sum:
            r -= 1
    return False


if __name__ == '__main__':
    test_arr = [10, 12, 23, 34, 45, 56, 67, 78]
    test_sum = 79
    x = find_integers_of_sum(test_arr, test_sum)
    print(x)