"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-conditional-statements/problem
"""


N = int(input().strip())

if (N >= 2 and N <= 5 and N%2 == 0):
    print('Not Weird')
elif (N > 20 and N%2 == 0):
    print('Not Weird')
else:
    print('Weird')
