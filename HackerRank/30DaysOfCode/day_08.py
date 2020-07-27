"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/submissions/code/66664346
"""


n = int(input())

phoneBook = {}
for x in range(n):
    x = input().split()
    phoneBook[x[0]] = x[1]

while True:
    try:
        q = input()
        if q in phoneBook:
            print("{0}={1}".format(q, phoneBook[q]))
        else:
            print("Not found")
    except:
        break
