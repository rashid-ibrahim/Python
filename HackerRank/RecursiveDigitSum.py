# Complete the superDigit function below.
def superDigit(n, k):
    n = str(n)
    if k == 1 and len(n) == 1:
        return int(n)

    n_list = [int(x) for x in n]

    n_sum = sum(n_list) * k

    if n_sum == 0:
        return 0

    return n_sum if len(str(n_sum)) == 1 else superDigit(n_sum, 1)


if __name__ == '__main__':
    answer = superDigit(9875, 4)

    print(answer == 8)
