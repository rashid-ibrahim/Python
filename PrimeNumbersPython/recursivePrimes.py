#Notes: This works as is. Needs memoization just for a speed concern and for
#the fun of adding it. Also make a non-recursive version to break the 1195
#limit. As it stands, just to get to that limit required increasing the recursion
#limit in python.

import math

def runAgain():
    again = input("Would you like to calculate another prime? ")

    if again[0].lower() == "y":
        main()
    else:
        return

def calcPrime(x, currNum, primeList):
    if currNum == 1:
        if 1 < x:
            currNum +=1
            calcPrime(x, currNum, primeList)
            return
    elif currNum == 2 or currNum == 3:
        primeList.append(currNum)
        if len(primeList) < x:
            currNum+=1
            calcPrime(x, currNum, primeList)
            return
    else:
        limit = math.trunc(math.sqrt(currNum))
        check = 0
        isPrime = True
        while check < len(primeList) and limit >= primeList[check]:
            if currNum%primeList[check] == 0:
                isPrime = False
                break
            check+=1
        
        if isPrime:
            primeList.append(currNum)
            
        currNum+=1
        if len(primeList) < x:
            calcPrime(x, currNum, primeList)
            return

    return primeList[-1]
    

def main():
    print()
    x = input("Please enter the position of the prime number you would" +
              "like to know: *Please note the number must be between 1 and 1195* ")
    if int(x):
        x = int(x)
    else:
        print("Please only enter NUMERICAL value.")
        main()
        return

    if x <= 0:
        print("Please only enter POSITIVE numbers.")
        main()
        return

    if x > 1195:
        print("This program will only calculate the first 1195 primes. " +
                      "Please enter a number less than 1196")
        main()
        return

    if x > 167:
        import sys
        sys.setrecursionlimit(10000)
        
    if x > 1:
            primeList = []
            nthPrime = calcPrime(x, 1, primeList)
    elif x == 1:
        nthPrime = 2

    print()
    print("The nth prime is: " + str(nthPrime))
    runAgain()
    print()
    return

if __name__ == "__main__":
    print("This program calculates the Nth prime number.")
    main()
