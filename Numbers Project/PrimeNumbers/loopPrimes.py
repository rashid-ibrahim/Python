#Notes: This works as is. Needs memoization just for a speed concern and for
#the fun of adding it.

import math

def runAgain():
    again = input("Would you like to calculate another prime? ")

    if again[0].lower() == "y":
        main()
    else:
        return

def calcPrime(x):
    if x == 2:
        return 3
    else:
        currNum = 5
        primeList = [2, 3]
        while x > len(primeList): # and limit >= primeList[check]:
            limit = math.trunc(math.sqrt(currNum))
            isPrime = True
            check = 0
            while check < len(primeList) and limit >= primeList[check]:
                if currNum%primeList[check] == 0:
                    isPrime = False
                    break
                check+=1
            if isPrime:
                if ((len(primeList)+1)%100000 == 0):
                    print("Prime number " + str(len(primeList)+1) + " is: " + str(currNum))
                primeList.append(currNum)
            
            currNum+=2

    return primeList[-1]
    

def main():
    print()
    x = input("Please enter the position of the prime number you would" +
              "like to know. ")
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

    if x > 1:
        nthPrime = calcPrime(x)
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
