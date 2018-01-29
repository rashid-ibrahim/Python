##################################################################################
# Author: Rashid "Lee" Ibrahim                                                   #
# Date: Jan 29, 2018                                                             #
# Program: Fibonacci Sequence Calculator                                         #
# Purpose: Calculates the nth fibonacci number either recursivly or itteratively #
##################################################################################


def fiboRecursive(ans, oldAns, curr, end):
    if curr != end+1:
        newAns = ans + oldAns
        return fiboRecursive(newAns, ans, curr+1, end)
    return (ans + oldAns)


def fiboLoop(n):
    ans = 1
    oldAns = 0
    for i in range(1, n+1):
        oldAns, ans = ans, ans+oldAns
    return ans


def main():
    x = int(input('Enter 1 for recursive fibonacci. Enter 2 for iterative fibonacci. '))
    y = int(input('What number would you like to calculate the fibonacci sequence out to? '))
    
    if x == 1:
        print('The', str(y), 'fibonacci number is', fiboRecursive(1, 0, 1, y))
    else:
        print('The', str(y), 'fibonacci number is', fiboLoop(y))
    
    return

if __name__ == '__main__':
    main()
