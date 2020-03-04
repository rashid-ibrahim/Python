"""
Problem Statement Found At: https://www.hackerrank.com/challenges/find-digits/problem

"""


def findDigits(n):

    list_n = [int(x) for x in str(n)]

    divisor_count = 0
    for i in list_n:
        if i != 0 and n % i == 0:
            divisor_count += 1

    return divisor_count


if __name__ == '__main__':
    x = findDigits(12)
    print(x)
