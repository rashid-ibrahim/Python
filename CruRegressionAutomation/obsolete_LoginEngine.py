#General Login Script.
#Some functions in this script would be better suited to be general purpose
#imported functions, so they can be used in other parts of the testing process.

import subprocess
#import win32gui
import pywin
import pyautogui

import GeneralFunctions as gen

#This will transform into get window focus/used for getting input fields
def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print ("Window %s:", win32gui.GetWindowText(hwnd))
    print ("\tLocation: (%d, %d)", (x, y))
    print ("\t    Size: (%d, %d)", (w, h))


#Function to click various buttons, Requires button label as input.
def click_buttons(button_label):
    return


#Function to return password field.
def getPasswordFocus():
    return

#Function to return username field.
def getUserNameFocus():
    return


#general engine function
def main():
    
    userName, userPass = gen.GetUNP()
    #print("foo")
    #print(userName)
    #print("userPass after function in main prog: ", userPass)
    halt = input()
    program = gen.launchCru()
    #positions = gen.getPositions()
    #print("blah")
    #print(position)
    #x = input()
    #while(x != "n"):
    #    x = input()
    #exit()
    windowArr = gen.getCruWindowLocations()

    userNameField = getUserNameFocus()
    userNameField.text(userName)

    passwordField = getPasswordFocus()
    passwordField.text(userPass)

    #Click submit button.

    #std_data = program.communicate(input='data_to_write')[0]

    #win32gui.EnumWindows(callback, None)
    input("Cru is now Logged in. Press Enter to continue.")


if __name__ == '__main__':
    main()
