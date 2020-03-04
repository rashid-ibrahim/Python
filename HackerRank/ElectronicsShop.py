"""
Problem Statement At: https://www.hackerrank.com/challenges/electronics-shop/problem
"""


def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    key_max = len(keyboards)
    drive_max = len(drives)

    for i in range(0, len(keyboards)):
        if keyboards[i] > b:
            key_max = i
            break

    for i in range(0, len(drives)):
        if drives[i] > b:
            drive_max = i
            break

    max_spend = 0

    for i in range(0, key_max):
        for j in range(0, drive_max):
            sum_val = keyboards[i] + drives[j]
            if max_spend < sum_val <= b:
                max_spend = sum_val
            elif sum_val >= b:
                break

    if max_spend == 0:
        return -1

    return max_spend


if __name__ == '__main__':
    test_keyboards = [3, 1]
    test_drives = [5, 2, 8]
    test_b = 10
    x = getMoneySpent(test_keyboards, test_drives, test_b)
    print('Expected: 539854')
    print(f'Actual: {x}')
