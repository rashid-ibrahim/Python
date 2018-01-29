#############################################################################
# Author: Rashid "Lee" Ibrahim                                              #
# Original Date: 4/26/2017                                                  #
# Most Recent Update: 4/27/2017                                             #
# Purpose: Script to get user name/pass word for use during testing session #
#############################################################################

import getpass

#Gets username/password to use for this testing session.
def getUserNameAndPass():
    #Might want to GUI this step.
    #Get User/Pass.. right now this is all hardcoded.
    #Might also use a default testing account for this.

    #Sanitization Goes Here
    UserName = ""
    PassWord = ""

    UserName = list(UserName)
    PassWord = list(PassWord)
    #print("Username:", UserName)
    #print("PassWord:", PassWord)
    #input()
    return UserName, PassWord


#Stops script from being run directly.
if __name__ == "__main__":
    print("This script can NOT be run directly")
    input()
    exit()

