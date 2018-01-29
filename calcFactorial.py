#################################################################
# Author: Rashid "Lee" Ibrahim                                  #
# Date: Jan 29, 2018                                            #
# Purpose: Recursively calculates the factorial for a number.   #
#################################################################

'''
*Note* This function uses recursion. Because of this, it is subject to python's
maxiumum recursion depth restraint. Keep this in mind when using this function.
'''
def getFactorial(ans, num):
    if num > 2:
        ans = getFactorial(ans, num -1)
    print("ans: " + str(ans))
    return (ans * num)

def main():
    num = int(input('Enter a number to get the factorial of: '))
    ans = 1
    print(getFactorial(ans, num))
    return 0

if __name__ == "__main__":
    main()
