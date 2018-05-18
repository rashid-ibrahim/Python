##################################################################################
# Author: Rashid "Lee" Ibrahim                                                   #
# Original Date: May 17, 2018                                                    #
# Last Modified: May 17, 2018                                                    #
# Program: Fibonacci Mem cached Memoize                                          #
# Purpose: Calculates the nth fibonacci number either recursivly or itteratively #
#          Adapted from base fibbo script                                        #
##################################################################################
from tempfile import mkdtemp
from joblib import Memory
from joblib import dump as dump
from joblib import load as load

cachedir = mkdtemp()
memory = Memory(cachedir=cachedir, verbose=0)


#@memory.cache
#memory.cache(memoizeFib = {})

try:
    memoizeFib = load(persistancy.txt)
    print('loaded file')
    print(memoizeFib)
except:
    print('did NOT load file')
    memoizeFib = {}

@memory.cache
def fiboRecursive(ans, oldAns, curr, end):
    print('new coldness')
    if curr != end+1: 
        newAns = ans + oldAns
        memoizeFib[curr] = newAns
        return fiboRecursive(newAns, ans, curr+1, end)
    return (ans + oldAns)


@memory.cache
def fiboLoop(ans, oldAns, dump, n):
    print('new hotness')
    for i in range(len(memoizeFib)+1, n+1):
        memoizeFib[i] = oldAns
        oldAns, ans = ans, ans+oldAns
    return ans

@memory.cache
def main():
    while True:
        x = int(input('Enter 1 for iterative fibonacci. Enter 2 for recursive fibonacci. '))
        y = int(input('What number would you like to calculate the fibonacci sequence out to? '))

        if y in memoizeFib:
            print('memoized answer found!')
            print('The {0} fibbonacci number is {1}'.format(y, memoizeFib[y]))
        else:
            if len(memoizeFib) > 1:
                ans = memoizeFib[len(memoizeFib)-1]
                oldAns = memoizeFib[len(memoizeFib)-1]
            else:
                ans = 1
                oldAns = 0
                
            if x == 1:
                print('The', str(y), 'fibonacci number is', fiboLoop(ans, oldAns, len(memoizeFib)+1, y))
            else:
                print('The', str(y), 'fibonacci number is', fiboRecursive(ans, oldAns, len(memoizeFib)+1, y))

        z = input('Run again? ')
        if z != '1' and z[0].lower != 'y':
            dump(memoizeFib, 'persistancy.txt')
            break
    
    return

if __name__ == '__main__':
    main()
