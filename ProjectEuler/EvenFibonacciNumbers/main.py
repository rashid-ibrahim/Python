
#Loop is off. This calcs the first N fibo numbers. Not the fibo numbers below N.
def evenSumFiboCalc(maxNum):
    sum = 0
    ans = 1
    oldAns = 0
    while ans <= maxNum:
        oldAns, ans = ans, ans+oldAns
        if ans%2 == 0:
            sum += ans
    return sum


def main():
    print('Calculating sum of even fibonacci numbers where number is < 4 million.')
    res = evenSumFiboCalc(4000000)
    print('The sum is {0}.'.format(res))
    return 0


if __name__ == "__main__":
    main()
