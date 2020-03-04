"""
Problem Statement Found At: https://www.hackerrank.com/challenges/the-birthday-bar/problem

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it.
She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth
month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can
divide the chocolate.

Consider the chocolate bar as an array of squares, s = [2, 2, 1, 3, 2]. She wants to find segments summing to Ron's
birthday, d = 4 with a length equalling his birth month, m = 2. In this case, there are two segments meeting her
criteria: [2, 2] and [1, 3] .

Function Description

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can
divide the chocolate bar.

birthday has the following parameter(s):

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month
"""


def birthday(s, d, m):
    if m == 1:
        return 0 if s.index(d) == -1 else s.count(d)

    count = 0

    for i in range(0, len(s)-m+1):
        if sum(s[i:i+m]) == d:
            count += 1

    return count


if __name__ == '__main__':
    # s_test = [1, 2, 1, 3, 2] d=3 m=4
    s_test = [int(x) for x in '2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1'.split(' ')]
    d_test = 18
    m_test = 7
    res = birthday(s_test, d_test, m_test)
    print(res)
