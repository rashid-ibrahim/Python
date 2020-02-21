"""
You are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
"""

'''
So the problem statement is not clear on if it is a sorted array or not.
For now I am assuming it is sorted already.
Mostly the only difference would be to first sort it.
'''


def find_missing(n, arr):
    for i in range(n):
        if arr[i] != i:
            return i


if __name__ == '__main__':
    test_arr = [0, 1, 3, 4, 5, 6]
    test_n = len(test_arr)
    x = find_missing(test_n, test_arr)
    print(x)
