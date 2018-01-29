#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/25/2017                                                  #
# Most Recent Update: 4/28/2017                                             #
# Purpose: Control script for general functions used during testing         #
#############################################################################

from time import sleep
import pyautogui as gui
gui.PAUSE = 1.0
gui.FAILSAFE = True

#Launches main CRU application.
def launchCru():
    from GeneralFunctions.openDestroyCru import launchCruApp
    return launchCruApp()


#Probably don't need this function.
def getCenter(item):
    center = gui.center(item)
    return center

#Gets list of desired tests.
def findTests():
    #base structure will probably be list the set of test and have the user in some way
    #pick them from a list. Probably would be best to do this step in GUI.
    return

def getImages(name):
    from GeneralFunctions.getImages import getImagePath
    return getImagePath(name)

def getUNP():
    from GeneralFunctions.GetUserNameAndPass import getUserNameAndPass
    return getUserNameAndPass()

def runStart():
    cruApp = launchCru()
    #get user name and pass here.
    loginCru()


#Stops script from being run directly.
if __name__ == '__main__':
    print("This script can NOT be run directly")
    input()
    exit()
