"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-loops/problem
"""


n = int(input().strip())
for i in range(1,11):
    print("{0} x {1} = {2}".format(n, i, n*i))