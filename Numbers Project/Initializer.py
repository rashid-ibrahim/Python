from BaseConversions import baseEngine
from EnglishBinaryConversion import binaryEngine
from BinaryAdditionSubtraction import binaryAddSub
from PrimeNumbers import loopPrimes

def runAgain():
    while 1==1:
        again = input("Would you like to run this program again? ")
    
        if again[0].lower() == "y":
            print()
            return 1
        elif again[0].lower() == "n":
            print()
            return 0
        else:
            print("Please only enter yes or no.")
            print()

def main():
    print("This program can convert any number from base ten to any base 1-16, " +
          "convert to or from binary, add or subtract binary numbers, and calculate" +
          "prime numbers.")
    print()

    x = 5
    while x > 0:
        x = input("Please choose between 0-3 for: 1 = Base Changes, 2 = " +
                  "Binary/String conversions, 3 = binary addition/subtraction," +
                  "4 = calculate a prime number or press 0 (zero) to exit. ")
        print()

        try:
            x = int(x)
            if x > 4 or x < 0:
                print("Please only enter 1, 2, 3, or 0" )
                print()
                raise Exception

            if x == 1:
                baseEngine.main()
                x = runAgain()
            elif x == 2:
                binaryEngine.main()
                x = runAgain()
            elif x == 3:
                binaryAddSub.main()
                x = runAgain()
            elif x == 4:
                loopPrimes.main()
                x = runAgain()
            elif x == 0:
                return
        except:
            x = runAgain()
    return

if __name__ == "__main__":
    main()
