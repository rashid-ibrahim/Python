"""
Problem Statement: https://www.hackerrank.com/challenges/bon-appetit/problem
"""


def bonAppetit(bill, k, b):
    bill2 = bill.copy()
    del bill2[k]
    bc = sum(bill2) / 2
    if int(bc) == b:
        print('Bon Appetit')
    else:
        print(int(b - bc))


if __name__ == '__main__':
    test_bill = [3, 10, 2, 9]
    test_k = 1
    test_b = 12

    bonAppetit(test_bill, test_k, test_b)