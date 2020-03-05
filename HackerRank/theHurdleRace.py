"""
Problem Statement Found At: https://www.hackerrank.com/challenges/the-hurdle-race/problem
"""


def hurdleRace(k, height):
    max_h = max(height)

    if max_h > k:
        return max_h - k
    return 0


if __name__ == '__main__':
    test_cases = [
        (4, [1, 6, 3, 5, 2], 2),
        (7, [2, 5, 4, 5, 2], 0),
    ]

    for case in test_cases:
        answer = hurdleRace(case[0], case[1])
        print(answer == case[2])
