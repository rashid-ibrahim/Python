"""
Problem Statement Here: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""


def sumOfDivisible(d, n):
    """
    I found this math formula online to calculate the sums in a non linear manner.
    This function is replacing the loop
        for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    """
    return d*(n/d)*((n/d)+1/2)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    # Solution Code
    sum_val = sumOfDivisible(3, n) + sumOfDivisible(5, n)

    print(sum_val)
