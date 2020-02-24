"""
Problem statement: https://www.hackerrank.com/challenges/kangaroo/problem
"""


def kangaroo(x1, v1, x2, v2):

    if x1 < x2:
        xlow, xhigh, vlow, vhigh = x1, x2, v1, v2
    else:
        xlow, xhigh, vlow, vhigh = x2, x1, v2, v1

    if (vlow < vhigh and xlow < xhigh) or (xlow != xhigh and vlow == vhigh):
        return 'NO'

    while xlow < xhigh:
        xlow += vlow
        xhigh += vhigh

        if xlow == xhigh:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    res = kangaroo(0, 3, 4, 2)
    print(res)