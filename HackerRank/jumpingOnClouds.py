
def jumpingOnClouds(c):
    jumps = 0
    size = len(c)-1
    loc = 0

    while loc < size:
        if loc + 2 <= size and c[loc + 2] == 0:
            loc += 2
        elif c[loc + 1] == 0:
            loc += 1

        jumps += 1

    return jumps


if __name__ == '__main__':
    test_c = [0, 0, 1, 0, 0, 1, 0]
    val = jumpingOnClouds(test_c)
    print(val)
