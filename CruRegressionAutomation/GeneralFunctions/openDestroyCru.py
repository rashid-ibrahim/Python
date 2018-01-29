#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/27/2017                                                  #
# Most Recent Update: 4/27/2017                                             #
# Purpose: Opens and closes cru application during testing                  #
#############################################################################

import subprocess
from time import sleep

def launchCruApp():
    #subprocess.call("C:\operations.jnlp", shell=True)
    cruProg = subprocess.Popen("C:\operations.jnlp", shell=True)
    return cruProg

def closeCru():
    return


#Stops script from being run directly.
if __name__ == "__main__":
    print("This script can NOT be run directly")
    input()
    exit()
