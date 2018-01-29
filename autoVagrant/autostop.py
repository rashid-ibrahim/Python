########################################################################################################
# Name: Auto stop vagrant machines script                                                              #
# Purpose: This script will automatically stop butr and dish vagrant machines.                         #
# Author: Rashid 'Lee' Ibrahim                                                                         #
# Date: 11/12/2017                                                                                     #
########################################################################################################

import os
from time import sleep
import subprocess as sub
import locations as loc

def machineHalt(d):
    os.chdir(d)
    sub.call("vagrant halt")
    sleep(5)
    return 0

def main():
    #Load Class
    l = loc.locations()

    machineHalt(l.getGala())
    machineHalt(l.getButr())
    machineHalt(l.getDish())

    return 0

if __name__ == "__main__":
    main()
