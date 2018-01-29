#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/28/2017                                                  #
# Most Recent Update: 4/28/2017                                             #
# Purpose: Script for testing Follow Up Selection portion of cru.           #
#############################################################################

import sys
sys.path.insert(0, '../GeneralFunctions')

import pyautogui as gui
import GeneralFunctions as gen

#Runs the tests.
def main():
    #Launch into follow up section of cru.
    gui.click(gui.center(gui.locateOnScreen(gen.getImages.getButtonsPath('FollowUp.png'))))
    
    #place holder return.
    return False

#Stops script from being run directly.
if __name__ == '__main__':
    print("This script can NOT be run directly")
    input()
    exit()
