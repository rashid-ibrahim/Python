##################################################################################
# Author: Rashid "Lee" Ibrahim                                                   #
# Date: Jan 29, 2018                                                             #
# Modified: May 05, 2016                                                         #
# Program: Fibonacci Sequence Calculator                                         #
# Purpose: Calculates the nth fibonacci number either recursivly or itteratively #
##################################################################################

memoizeFib = {}

def fiboRecursive(ans, oldAns, curr, end):
    if curr != end+1: 
        newAns = ans + oldAns
        memoizeFib[curr] = newAns
        return fiboRecursive(newAns, ans, curr+1, end)
    return (ans + oldAns)


def fiboLoop(ans, oldAns, n):
    for i in range(len(memoizeFib)+1, n+1):
        memoizeFib[i] = oldAns
        oldAns, ans = ans, ans+oldAns
    return ans


def main():
    while True:
        x = int(input('Enter 1 for recursive fibonacci. Enter 2 for iterative fibonacci. '))
        y = int(input('What number would you like to calculate the fibonacci sequence out to? '))

        print('\n')
        print('memoizeFib')
        print(memoizeFib)
        print('\n')
        if y in memoizeFib:
            print('memoize found')
            print('The {0} fibbonacci number is {1}'.format(y, memoizeFib[y]))
            print(memoizeFib[8])
        else:
            if len(memoizeFib) > 1:
                ans = memoizeFib[len(memoizeFib)-1]
                oldAns = memoizeFib[len(memoizeFib)-1]
            else:
                ans = 1
                oldAns = 0
                
            if x == 1:
                print('The', str(y), 'fibonacci number is', fiboRecursive(ans, oldAns, len(memoizeFib)+1, y))
            else:
                print('The', str(y), 'fibonacci number is', fiboLoop(ans, oldAns, y))

        z = input('Run again? ')
        if z != 'y' and z != 'yes':
            break
    
    return

if __name__ == '__main__':
    main()
