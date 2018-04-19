########################################################################################################
# Name: Auto start vagrant machines script                                                             #
# Purpose: This script is to auto load the butr and dish vagrant machines and then run grunt on them.  #
# Author: Rashid 'Lee' Ibrahim                                                                         #
# Date: 11/12/2017                                                                                     #
########################################################################################################

import os
from time import sleep
import subprocess as sub
import locations as loc
import MachineLoader as mac

def bootMachine(d):
    os.chdir(d)
    sub.call("vagrant up")
    sleep(5)
    return 0

def main():
    l = loc.locations()
    m = mac.MachineLoader()
    machines = m.getUserChoice()

    if machines['Gala'] == True:
        bootMachine(l.getGala())
        
    if machines['butr'] == True:
        bootMachine(l.getButr())
        
    if machines['dish'] == True:
        bootMachine(l.getDish())
    
    if machines['but'] == True:
        gruntLoad(l.getButr())
        
    return 0

if __name__ == "__main__":
    main()
