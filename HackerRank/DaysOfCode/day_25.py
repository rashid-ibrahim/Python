"""
Problem Statement At: https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
"""

known_primes = [1, 2, 3]
not_primes = []


def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        not_primes.append(num)
        print('Not prime')
        return

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            not_primes.append(num)
            print('Not prime')
            return
        i = i + 6

    known_primes.append(num)
    print('Prime')


cases = int(input())

for _ in range(cases):
    test = int(input())

    if test == 1:
        print('Not prime')
        continue

    if test in known_primes:
        print('Prime')
    elif test in not_primes:
        print('Not prime')
    else:
        is_prime(test)
