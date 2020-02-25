"""
Problem Statement: https://www.hackerrank.com/challenges/drawing-book/problem
"""


def pageCount(n, p):
    if n == 1 or n == p or p == 1:
        return 0

    middle = int(n / 2)

    front = [i for i in range(0, middle+1)]
    pages = []

    if p in front:
        curr_page = 0
        while curr_page < middle:
            pages.append([curr_page, curr_page+1])
            curr_page += 2
    else:
        if middle % 2 == 0:
            curr_page = middle
        else:
            curr_page = middle+1

        while curr_page < n+1:
            pages.append([curr_page, curr_page+1])
            curr_page += 2
        pages.reverse()

    for i in range(0, len(pages)):
        if p in pages[i]:
            return i


if __name__ == '__main__':
    x = pageCount(5, 4)  # 0
    # pageCount(6, 2)  # 1
    # x = pageCount(6, 5)
    # x = pageCount(7, 4)  # 1
    # x = pageCount(37455, 29835)  # 3810
    print(x)
