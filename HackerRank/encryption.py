"""
Problem Statement Found At: https://www.hackerrank.com/challenges/encryption/problem
"""

import math


def encryption(s):
    s = s.replace(' ', '')
    cs = math.ceil(math.sqrt(len(s)))
    s_matrix = []

    while len(s) > cs:
        s_matrix.append(s[0:cs])
        s = s[cs:]

    s_matrix.append(s)

    out = [''] * cs
    cs_count = 0

    while cs_count < cs:
        for i in range(len(s_matrix)):
            if s_matrix[i] and len(s_matrix[i]) > 1:
                out[cs_count] += s_matrix[i][0]
                s_matrix[i] = s_matrix[i][1:]
            else:
                out[cs_count] += s_matrix[i]
                s_matrix[i] = ''

        cs_count += 1

    return ' '.join(out)


if __name__ == '__main__':
    test_strings = [
        ('haveaniceday', 'hae and via ecy'),
        ('feedthedog', 'fto ehg ee dd'),
        ('chillout', 'clu hlt io'),
    ]

    run_tests = [1]

    for test in run_tests:
        answer = encryption(test_strings[test][0])
        print(answer == test_strings[test][1])
