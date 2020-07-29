"""
Problem Statement Found at: https://www.hackerrank.com/challenges/30-scope/problem
"""


# ####Begin Auto Generated code.####
class Difference:
    def __init__(self, a):
        self.__elements = a
    # ####End Auto Generated code.####

    # Add your code here
    def computeDifference(self):
        self.__elements.sort()
        # I know declaring an instance var here is NOT pep8 compliant, but it's what the problem specifically asked for.
        self.maximumDifference = abs(self.__elements[-1] - self.__elements[0])