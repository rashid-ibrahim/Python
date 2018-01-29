#Needs some clean up here and there, mostly just in the display of results.
#Also a few comments here and there about some optimization things.

import re

def convToBinary(rawIn):
    #needs work. numbers to binary only does one digit at a time. so no numbers
    #higher than 9. ex 123 = 00110001 00110010 00110011 three different binary
    #numbers.
    rawIn = " ".join(format(ord(x), 'b') for x in rawIn)
    rawIn = rawIn.split(" ")
        
    clean = ""
    for i in range(len(rawIn)):
        while len(rawIn[i]) < 8:
            rawIn[i] = "0" + rawIn[i]
            
    clean = " ".join(map(str, rawIn))
    print(clean)
    print()
    return

def convToEnglish(rawIn):
    clean = ""
    for i in range(len(rawIn)):
        temp = rawIn[i]
        totVal = 0
        
        if temp[0] == "1":
            totVal += 128
        if temp[1] == "1":
            totVal += 64
        if temp[2] == "1":
            totVal += 32
        if temp[3] == "1":
            totVal += 16
        if temp[4] == "1":
            totVal += 8
        if temp[5] == "1":
            totVal += 4
        if temp[6] == "1":
            totVal += 2
        if temp[7] == "1":
            totVal += 1
            
        clean += str(chr(totVal))
    
    print("clean " + clean)
    print()
    return

def inputEngine():
    rawIn = ""
    rawIn = input("Please enter the string or binary you would like to have " +
                  "translated. ")

    if rawIn == "":
        print("You must enter something to be converted")
        return 1
    else:
        binary = True
        try:
            int(rawIn)
            negFlag = ""
            if rawIn[0] == "-":
                rawIn = rawIn.splice(-1)
                negFlag = "-"
            for i in range(len(rawIn)):
                print("bin3")
                if rawIn[i] != " ":
                    temp = rawIn[i]
                else:
                    temp = None
                if temp is not None:
                    print("bin4")
                    if (int(temp) != 0) and (int(temp) != 1):
                        binary = False
            
        except:
            binary = False

        if binary == True:
            for i in range(len(rawIn)):
                print("rawIn[i]: " + str(rawIn[i]))
                print(len(str(rawIn[i])))
                if len(str(rawIn[i]))%8 != 0:
                    #need to implement long string format.
                    print("Please enter binary numbers in either 8 bit format or " +
                          "8 bit binary in one long string")
                    return 1
            convToEnglish(rawIn)
        else:
            convToBinary(rawIn)
    return 0

def main():
    x = 1
    while x == 1:
        x = inputEngine()

    return

if __name__ == "__main__":
    main()
