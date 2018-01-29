#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/25/2017                                                  #
# Most Recent Update: 4/28/2017                                             #
# Purpose: Main Testing Engine                                              #
#############################################################################

import GeneralFunctions as gen
import pyautogui as gui
gui.PAUSE = 0.5
gui.FAILSAFE = True
from time import *

#Cru Specific Tests
def cruTests():
    import CruSpecific
    testResults = CruSpecific.startTests()
    print(testResults)
    return False
    
#Generic Application Launcher and Login.
def main():
    cruApp = gen.launchCru()

    #Checks for memory runtime error. This is a problem with low memory
    #on the test machine and not with the cru application.
    if gui.locateOnScreen(gen.getImages('RunTimeError.png')):
        gui.click(gui.locateOnScreen(gen.getImages('OkButton.png')))

    #Nested If Statement to check for two java security messages in Windows 10.
    if gui.locateOnScreen(gen.getImages.getImagePath(('SecurityWarning1.png'))):
        #Get location of AcceptSecurityWarn pic. Move mouse rel to that location.
        #click mouse.
        acceptTup = gui.locateOnScreen(gen.getImages.getImagePath('AcceptSecurityWarning.png'))
        gui.moveTo(acceptTup[0], acceptTup[1])
        gui.click(gui.moveRel(18,18))
        gui.moveTo(acceptTup[0], acceptTup[1])
        gui.click(gui.moveRel(388,19))
        time.sleep(1.5)
        if gui.locateOnScreen(gen.getImages('SecurityWarning2.png')):
            acceptTup = gui.locateOnScreen(gen.getImages.getImagePath('AcceptSecurityWarning.png'))
            gui.moveTo(acceptTup[0], acceptTup[1])
            gui.click(gui.moveRel(18,18))
            gui.moveTo(acceptTup[0], acceptTup[1])
            gui.click(gui.moveRel(388,19))

    mainAppOnScreen = False
    #Pauses Script While Application Launches.
    count = 0
    while mainAppOnScreen == False or count < 100000:
        count +=1
        if gui.locateOnScreen(gen.getImages.getImagePath('LaunchScreen.png')):
            mainAppOnScreen = True
        else:
            pass
            
    #Gets Username and Password and fills appropriate boxes.
    UserName, Password = gen.getUNP()
    #need to add locating box when stuff is typed into the program
    userNameSelected = False
    count = 0
    while userNameSelected == False or count < 0:
        try:
            gui.click(gui.center(gui.locateOnScreen(gen.getImages.getImagePath('UserNameBox.png'))))
            userNameSelected = True
        except (e):
            pass
    gui.typewrite(UserName)

    #same addition needed here, also add code to clear them by default
    gui.click(gui.center(gui.locateOnScreen(gen.getImages.getImagePath('PasswordBox.png'))))
    gui.typewrite(Password)

    #Finds and clicks 'ok' button.
    cruOkButton = gui.locateOnScreen(gen.getImages.getImagePath('OkButton.png'))
    gui.click(gui.center(cruOkButton))
    time.sleep(0.9)


    #Need to add getting desired test here. Or maybe before start. Right now they all will run.
    #Launches Program Specific Testing.
    results = cruTests()
    for i in range(len(results)):
        print(results[i])
    return False


#Stops script from being run directly.
if __name__ == "__main__":
    main()
