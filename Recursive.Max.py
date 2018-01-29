#Name: Rashid "Lee" Ibrahim
#Date: July 22 2014
#Application: Assignment 8.1 Recursive.Max.py
#Purpose: Write and test a recursive function max to find the largest number in a list.
        # The max is the largest of the first item and the max of all the other items.

#Main function.
def main():
    #Gets input from the user for a set of numbers.
    numbers = input("Please input  a set of numbers to find the" +
                          " max value of (seperated by a comma): ")

    #Splits the input numbers intwo a list.  
    strList = numbers.split(",")

    #Gets the length of the input list.
    c = len(strList)
    #Creates an empty integer list to hold converted values.
    numList = [0] * c
    #Variable used to count itterations.
    i = 0

    #While ierations less than the count, this loop runs.
    while i < c:
        #Tries to convert the current string list item to a numeric value and
        #places it into the numeric list.
        try:
            #Actual conversion.
            numList[i] = int(strList[i])
        #If the input item is not numeric, this catches.
        except:
            #Prints to user.
            print("Please only input numeric values")
            #Blank line.
            print()
            #Restarts the program.
            main()
        #Adds to the counter each itteration.
        i += 1
    #Inittially sets the high to the first list item.
    currentHigh = numList[0]
    #Loops through each item in the numList and compares them to the currentHigh.
    for i in numList:
        #Sets the currentItem each itteration.
        currentItem = i
        #Checks if the currentItem is higher than the currentHigh.
        if currentItem > currentHigh:
            #If the current item is higher than the high value, it becomes the high.
            currentHigh = currentItem

    #Prints of the calculated high number.            
    print("The high number of the list is ", currentHigh)

#Initial load of the program.
main()
