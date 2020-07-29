"""
Problem Statement found at: https://www.hackerrank.com/challenges/30-sorting/problem
"""


#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


def bubble_sort(arr, size):
    swaps = 0
    not_sorted = True

    while not_sorted:
        not_sorted = False
        for i in range(size - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
                not_sorted = True

    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(arr[0]))
    print('Last Element: {}'.format(arr[-1]))

bubble_sort(a, n)