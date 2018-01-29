#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/25/2017                                                  #
# Most Recent Update: 4/28/2017                                             #
# Purpose: Sets The Image Path Folders                                      #
#############################################################################

import sys
sys.path.insert(0, '/GeneralFunctions')
import GeneralFunctions as gen
import os
import pyautogui as gui

#Returns Default Image Folder Path with the Given Image Name.
def getImagePath(name):
    path = os.path.dirname(os.path.dirname(__file__))
    path += "\\ScreenShots\\"
    return path + name

#Returns The Button Folder Path inside of the Image Folder with the Given Button Name.
def getButtonsPath(buttonName):
    buttonsPath = getImagePath("Buttons")
    buttonsPath = buttonsPath + "\\" + buttonName
    return buttonsPath

#Stops script from being run directly.
if __name__ == '__main__':
    print("This script can NOT be run directly")
    input()
    exit()
