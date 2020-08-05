"""
Problem Statement At: https://www.hackerrank.com/challenges/30-bitwise-and/problem
"""


def main(input_n, max_range):
    """
    So I tried this brute force solution but it ended up being slow and clunky.
    Because of that, I switched to the one liner below, but I wanted to preserve this code for a look at
    nested looping.
    """
    S = [i+1 for i in range(input_n)]
    max_val = 0

    for i in S:
        for j in S:
            test = i & j
            if max_range > test > max_val:
                max_val = test

    return max_val


if __name__ == '__main__':
    # These are test cases that are defined in the problem statement.
    n = [5, 8, 2]
    k = [2, 5, 2]

    for z in range(3):
        # largest = main(n[z], k[z])

        # This is the one liner. Instead of doing bit wise and, it uses the OR operator. This lets us not have to loop
        # through the array as many times.
        print(k[z]-1 if ((k[z]-1) | k[z]) <= n[z] else k[z]-2)
