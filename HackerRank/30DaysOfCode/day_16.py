"""
Problem Statement At: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?h_r=next-challenge&h_v=zen
"""


try:
    S = int(S)
    print(S)

except ValueError:
    print('Bad String')