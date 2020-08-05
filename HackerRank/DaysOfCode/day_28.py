"""
Problem Statement at: https://www.hackerrank.com/challenges/30-regex-patterns/problem
"""

# Begin Auto Generated Code
if __name__ == '__main__':
    N = int(input())

    # End Auto Generated Code
    names = []
    # Begin Auto Generated Code
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        # End Auto Generated Code

        if '@gmail.com' in emailID:
            names.append(firstName)

    names.sort()

    [print(name) for name in names]
