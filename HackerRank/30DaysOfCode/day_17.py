"""
Problem Statement Found at: https://www.hackerrank.com/challenges/30-more-exceptions/problem
"""


class Calculator:
    @staticmethod
    def power(n, p) :
        try:
            if n < 0 or p < 0:
                raise ValueError
            return n**p
        except ValueError:
            return 'n and p should be non-negative'

