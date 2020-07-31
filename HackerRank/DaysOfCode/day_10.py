"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""

print(len(max(bin(int(input().strip()))[2:].split('0'))))