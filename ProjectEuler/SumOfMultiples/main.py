import SumOfMultiples

def getInput():
    x = input('Enter in the format X, Y, Z or type Exit to leave. ')
    if isinstance(x, str) and x.lower() == 'exit':
        return 'exit'

    x = x.split(', ')
    if len(x) != 3:
        print ('You did not enter the numbers in the format X, Y, Z... EXAMPLE: 3, 5, 100')
        return getInput()

    for i in range(len(x)):
        try:
            x[i] = int(x[i])
        except(e):
            print("The value {0} is not a valid number".format(x[i]))
            return getInput()

    if x[0] > x[2] or x[1] > x[2]:
        print('Both of the first two numbers MUST be smaller than the third!')
        print('You entered {0}, {1}, and {2}. This is NOT valid'.format(x[0],x[1],x[2]))
        return getInput()

    return x

def getOutPut(arrIn):
    smClass = SumOfMultiples.SumOfMultiples(arrIn[0],arrIn[1],arrIn[2])
    return smClass.getSum()


def main():
    while True:
        x = getInput()
        if x == 'exit':
            return
        else:
            res = getOutPut(x)
            print('The sum of the multiples of both {0} and {1} is the number: {2}'.format(x[0],x[1],res))
    return 0

if __name__ == "__main__":
    main()
