"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-arrays/problem
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
start, end = 0, len(arr)-1

# Alternatively this code could be replaced with the reverse method, but that was not the intention of this challenge.
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(' '.join([str(x) for x in arr]))