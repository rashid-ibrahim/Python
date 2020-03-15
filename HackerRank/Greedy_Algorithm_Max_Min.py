"""
Problem Statement Found At: https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms&isFullScreen=true
"""
import sys


def maxMin(k, arr):
    arr = sorted(arr)
    low_diff = sys.maxsize
    for i in range(len(arr)-k+1):
        diff = arr[i+k-1] - arr[i]
        if diff < low_diff:
            low_diff = diff

    return low_diff
