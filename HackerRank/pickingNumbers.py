"""
Problem Statement Found At: https://www.hackerrank.com/challenges/picking-numbers/problem
"""

def pickingNumbers(a):
    a.sort(reverse=True)
    val = a.pop()
    set_counts = [1]

    while a:
        if val == a[-1] or val == a[-1] - 1:
            set_counts[-1] += 1
        else:
            set_counts.append(1)
            val = a[-1]

        a.pop()

    return max(set_counts)


if __name__ == '__main__':
    test_a = [4, 6, 5, 3, 3, 1]  # answer = 3
    test_b = [1, 2, 2, 3, 1, 2]  # answer = 5
    answer = pickingNumbers(test_b)
    print(answer == 5)

