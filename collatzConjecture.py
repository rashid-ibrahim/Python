
def conjecture(calcNum):
    steps = 0
    while calcNum > 1:
        if calcNum % 2 == 0:
            calcNum = calcNum/2
        else:
            calcNum = (calcNum*3)+1
        steps+=1
    return steps

def main():
    calcNum = int(input("Enter the number: "))

    if calcNum > 1:
        steps = conjecture(calcNum)

    if calcNum == 1:
        print("No steps to reach number 1 because you entered number 1")
    elif calcNum == 1:
        print("It took one step to reach number 1 because you entered number 2.")
    else:
        print("It took " + str(steps) + " steps to reach number 1 because you entered " + str(calcNum))

if __name__ == "__main__":
    main()
