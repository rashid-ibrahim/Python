    
def mergList(answerList, base):
    answerList = "".join(map(str,answerList))

    if base <= 10:
        answerList = [int("".join(answerList))]
    return answerList

def baseConv(origNum, base):
    negFlag = False
    if origNum < 0:
        origNum = orignNum*-1 #int(str(origNum).strip("-"))
        negFlag = True
    answer = []
    if base <= 10:
        while origNum > 0:
            answer.insert(0,int(origNum%base))
            origNum = origNum//base
    else:
        while origNum > 0:
            if origNum%base == 10:
                answer.insert(0,"A")
            elif origNum%base == 11:
                answer.insert(0,"B")
            elif origNum%base == 12:
                answer.insert(0,"C")
            elif origNum%base == 13:
                answer.insert(0,"D")
            elif origNum%base == 14:
                answer.insert(0,"E")
            elif origNum%base == 15:
                answer.insert(0,"F")
            else:
                answer.insert(0,origNum%base)
            origNum = origNum//base
    if negFlag == True:
        answer.insert(0,"-")
    answer = mergList(answer, base)
    
    return answer

def main():
    rawIn = input("Please enter your number to be converted: ")

    try:
        origNum = int(rawIn)
    except:
        print("Please only enter NUMERICAL value.")
        print()
        main()
        return

    if origNum == 1 or origNum == -1:
        print("The number " + str(origNum) + " in all bases is always " +
              str(origNum) + ".")
    else:
        for i in range(2, 17):
            if i == 2:
                baseType = "(binary)"
            elif i == 8:
                baseType = "(octal)"
            elif i == 16:
                baseType = "(hexadecimal)"
            else:
                baseType = ""
                
            print("The number " + str(origNum) + " in base " + str(i) +  baseType +
                  " is: " + str(baseConv(origNum, i)).strip('[]'))

        print()
        return
