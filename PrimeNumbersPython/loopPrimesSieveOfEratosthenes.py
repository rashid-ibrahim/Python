#Needs memoization just for a speed concern and for
#the fun of adding it.

import math

def runAgain():
    again = input("Would you like to calculate another prime? ")

    if again[0].lower() == "y":
        main()
    else:
        return

def calcPrime(x):
    if x == 1:
        return 2
    elif x == 2:
        return 3
    else:
        primeList = [2, 3]
        for i in range(x-1):
            j = 5
            if j != 1 and j%2 != 0 and j%3 != 0:
                primeList.append(j)
            j+=2

        for i in range(len(primeList)):
            print("primeList(" + str(i) + "): " + str(primeList[i]))
        for i in range(len(primeList)):
            j = 1
            while j < len(primeList):
                if primeList[i]%primeList[j] == 0:
                    del primeList[i]
                j+=1
                print("len(primeList): " + str(len(primeList)))
                print("j: " + str(j))
                #elif primeList[i]%100000 == 0:
                #    print("Prime number " + str(len(primeList)+1) + " is: " + str(primeList[i]
    
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
