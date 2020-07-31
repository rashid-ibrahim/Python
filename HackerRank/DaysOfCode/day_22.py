"""
Problem Statement Found at: https://www.hackerrank.com/challenges/30-binary-search-trees/problem
"""


def getHeight(self, root):
    if root is None:
        return -1
    else:
        left_depth = self.getHeight(root.left)
        right_depth = self.getHeight(root.right)

        return left_depth + 1 if left_depth > right_depth else right_depth + 1