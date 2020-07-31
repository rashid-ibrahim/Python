"""
Problem Statement at: https://www.hackerrank.com/challenges/30-interfaces/problem
"""


# ####Begin Auto Generated Code####
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
# ####End Auto Generated Code####


class Calculator(AdvancedArithmetic):
    @staticmethod
    def divisorSum(n):
        # This is a quick and dirty method to get the factors.
        # For larger numbers, you would want to implement a factorization algorithm

        total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                total += i

        return total
