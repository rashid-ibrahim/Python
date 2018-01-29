#Name: Rashid "Lee" Ibrahim
#Date: July 15 2014
#Application: Final math.py
#Purpose: Final Project. Simple math game that gives a problem and accepts user
        # input for a result. The result is then checked for correctness.

#Imports modules used.
from graphics import *
from button import *
import random

#Sets global variables.
qtextStore = " "
txtResult = " "
qasked = 0

#Class to determine the math operator.
class operator():
    #Function to randomly generate an operator.
    def oper():
        #Creates a random integer.
        rand = random.randint(1,4)
        #Test code.
        #print("oper rand: ", rand)
        #If statement to determine which operator to used based on the random integer.
        if rand == 1:
            #If the integer is 1 the operator is addition.
            op = "+"
            #Test code.
            #print("oper op: ", op)
            return op
        elif rand == 2:
            #If the integer is 2 the operator is subtraction.
            op = "-"
            #Test code.
            #print("oper op: ", op)
            return op
        elif rand == 3:
            #If the integer is 3 the operator is multiplication.
            op = "*"
            #Test code.
            #print("oper op: ", op)
            return op
        else:
            #Else if the integer is 4 the operator is division.
            op = "/"
            #Test code.
            #print("oper op: ", op)
            return op

    #Function performing the operation.
    def operation(num1, num2, op):
        #Adds the numbers if the operator is addition.
        if op == "+":
            answer = num1 + num2
            #Test code.
            #print("operation answer: ", answer)
            #print("operation op: ", op)
            return answer
        #Subtracts the numbers if the operator is subtraction.
        elif op == "-":
            answer = num1 - num2
            #Test code.
            #print("operation answer: ", answer)
            #print("operation op: ", op)
            return answer
        #Multiplies the numbers if the operator is multiplication.
        elif op == "*":
            answer = num1 * num2
            #Test code.
            #print("operation answer: ", answer)
            #print("operation op: ", op)
            return answer
        #Else divides the numbers.
        else:
            answer = num1 / num2
            #Test code.
            #print("operation answer: ", answer)
            #print("operation op: ", op)
            answer = round(answer, 3)
            return answer


def ask(win):
    #Generates a variable between 1 and 100 for the first number.
    num1 = random.randint(1, 100)
    #Generates a variable between 1 and 100 for the second number.
    num2 = random.randint(1, 100)
    #Calls the operator function to generate the operator variable.
    op = operator.oper()
    #Test code.
    #print("ask op: ", op)
    #Generates the answer from the answer function.
    answer = operator.operation(num1, num2, op)
    #Test code.
    #print("answer: ", answer)
    #Imports the global question variable into this function.
    global qtextStore
    #Checks the question variable for successive runs of the program.
    if qtextStore != " ":
        qtext = qtextStore
        qtext.undraw()
        qtext = Text(Point(300,115), (str(num1) + " " + str(op) + " " +str(num2) + "?"))
        qtextStore = qtext
        qtext.draw(win)
    #If this is the first question asked this code runs.
    else:
        qtext = Text(Point(300,115), (str(num1) + " " + str(op) + " " +str(num2) + "?"))
        qtext.draw(win)
        qtextStore = qtext
    return answer

#Function to check the answer typed in.
def checkAnswer(win, userAnswer, answer):
    #Imports the global variable for the answer.
    global txtResult
    #Checks to see if the results box is empty.
    if txtResult != " ":
        txtResult.undraw()
    #Checks to see the user has typed in an answer.
    if len(userAnswer) == 0:
        txtResult = Text(Point(300,200),"Need to enter some numbers!")
        txtResult.draw(win)
        #imports global variable.
        global qasked
        #Resets the qasked variable so the user may try to answer the question again.
        qasked = 1
        return
    #Checks if the user typed answer does NOT match the generated answer.
    elif float(userAnswer) != answer:
        txtResult = Text(Point(300,200),"The correct answer is: " + str(answer))
        txtResult.draw(win)
        return
    #Else the answer is correct.
    else:
        txtResult = Text(Point(300,200),"That is correct!")
        txtResult.draw(win)
        return
#Function to draw the GUI.
def drawGUI():
    win = GraphWin("Simple Math", 500,300)
    win.setBackground("lightyellow")
    greet = Image(Point(250,30), "logo.gif")
    greet.draw(win)
    prompt = Text(Point(130,160), "Type your answer here:")
    prompt.setSize(13)
    prompt.draw(win)
    instruct = Text(Point(250,60), "Press the 'Ask a question' button to begin solving a math problem.")
    instruct.setSize(13)
    instruct.draw(win)
    note = Text(Point(250,80), "Note: Division is rounded to 3 decimals")
    note.setSize(9)
    note.draw(win)
    return win

#Function to draw and activate the buttons.
def drawButtons(win):
    askq = Button(win, Point(125,115), 110, 25, "Ask a question")
    askq.activate()
    check = Button(win, Point(125,200), 110, 25, "Check Results")
    check.activate()
    close = Button(win, Point(125,250), 110, 25, "Exit")
    close.activate()
    return askq, check, close

#Main function that runs when the program loads.
def main():
    #Calls function to draw GUI.
    win = drawGUI()
    #Sets variable and draws input box for user answer.
    result = Entry(Point(290,160), 15)
    result.setFill("white")
    result.draw(win)
    #Calls function to draw the buttons.
    askq, check, close = drawButtons(win)
    #Imports global variables.
    global qasked
    global qtextStore
    #Continuously checks for user mouse clicks.
    while True:
        #Gets the user mous click position.
        click = win.getMouse()
        #Checks which button is clicked.
        if askq.clicked(click) == True:
            answer = ask(win)
            #Sets a variable used to see if a question has been asked.
            qasked = 1
        #Runs when the check answer button is clicked.
        elif check.clicked(click) == True and qasked == 1:
            userAnswer = result.getText()
            #Sets qasked back to 0 so that the user must ask a new question after checking the answer for this one.
            qasked = 0
            checkAnswer(win, userAnswer, answer)
        #This runs if the user tries to check an answer before asking a new question.
        elif check.clicked(click) == True and qasked == 0:
            #Changes the text displayed based on if the user has not asked a question at all or is just trying to answer the same one.
            if qtextStore != " ":
                qtext = qtextStore
                qtext.undraw()
                qtext = Text(Point(300,115), "Please ask a new question first")
                qtextStore = qtext
                qtext.draw(win)
            else:
                qtext = Text(Point(300,115),"Please ask a question first")
                qtext.draw(win)
                qtextStore = qtext
        #Runs if the user clicks the close button.
        elif close.clicked(click) == True:
            win.close()

#Initial run of the program.
while True:
    main()
