"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-binary-numbers/submissions/code/66665161
"""

print(len(max(bin(int(input().strip()))[2:].split('0'))))