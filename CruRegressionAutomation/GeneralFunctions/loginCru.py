#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/25/2017                                                  #
# Most Recent Update: 4/27/2017                                             #
# Purpose: Initial Login of Cru Application before testing can begin        #
#############################################################################

import pyautogui as gui

def loginCru():
    cruUserName = gui.locateOnScreen('../ScreenShots/UserNameBox.png')
    cruPassword = gui.locateOnScreen('../ScreenShots/PasswordBox.png')


#Stops script from being run directly.
if __name__ == "__main__":
    print("This script can NOT be run directly")
    input()
    exit()
