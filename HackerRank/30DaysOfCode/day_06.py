"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-review-loop/problem
"""


t = int(input())
output = []

for x in range(0,t):
    stringIn = input()
    odd = ""
    even = ""
    for y in range(len(stringIn)):
        if y%2 != 0:
            odd += stringIn[y]
        else:
            even += stringIn[y]
    print(even, odd)