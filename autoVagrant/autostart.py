########################################################################################################
# Name: Auto start vagrant machines script                                                             #
# Purpose: This script is to auto load the butr and dish vagrant machines and then run grunt on them.  #
# Author: Rashid 'Lee' Ibrahim                                                                         #
# Date: 11/12/2017                                                                                     #
# Modified: 05/15/2018                                                                                 #
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


#grunt doesn't continue to watch because the console closes when the program ends
#need to find a way to leave the console open.
def gruntLoad(d):
    os.chdir(d + '\www\public')
    sub.call("grunt watch", shell=True)
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

    if machines['butr'] == True:
        gruntLoad(l.getButr())
        
    raise Exception('exit')
    #return 0

if __name__ == "__main__":
    main()
