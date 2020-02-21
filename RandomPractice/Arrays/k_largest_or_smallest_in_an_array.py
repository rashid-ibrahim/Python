"""
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3
then your program should print 50, 30 and 23.
"""


def k_largest(arr, k):
    # we check size here to only do it once.
    size = len(arr)

    for i in range(0, size):
        for j in range(0, size-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr[-k:]


if __name__ == '__main__':
    x = k_largest([1, 23, 12, 9, 30, 2, 50], 3)
    print(x)