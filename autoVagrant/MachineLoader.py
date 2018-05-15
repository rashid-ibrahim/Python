########################################################################################################
# Name: Auto start vagrant machines script                                                             #
# Purpose: Class file handles user I/O for vagrant machine loading                                     #
# Author: Rashid 'Lee' Ibrahim                                                                         #
# Date: 11/12/2017                                                                                     #
########################################################################################################


import os
from time import sleep
import subprocess as sub
import locations as loc

class MachineLoader:
    def __init__(self):
        self.cases = {}
        self.userResponse = int()
        self.response = {
                            "Gala" : False,
                            "butr" : False,
                            "dish" : False,
                        }
        self.loc = loc

        #self.getUserChoice()
        
    def getCases(self):
        self.cases = {
                        1 : 'Gala Only',
                        2 : 'Gala and butr',
                        3 : 'Gala, butr, and dish',
                        4 : 'butr and dish',
                        5 : 'butr only',
                     }
        return self.cases
    
    def getUserChoice(self, level=0):
        print('Enter the option for machines you would like booted: ')
        cases = MachineLoader.getCases(self)
        for i in range(1, len(cases)+1):
            print(str(i) + ". " + cases[i])
        x = input("Select Choice: ")
        try:
            x = int(x)
            if x < 1 or x > 5:
                raise ValueError('That is not a valid number')

            self.userResponse = x
            self.getResponse(x)
            return self.response
        except Exception as e:
            print(e)
            print('')
            print('')
            if level <=2:
                getUserChoices(self, level)
            else:
                input("Too many wrong inputs in a row! The program will now exit!")
                exit()

    def getResponse(self, x):
        if x == 1:
            self.response['Gala'] = True
        elif x == 2:
            self.response['Gala'] = True
            self.response['butr'] = True
        elif x == 3:
            self.response['Gala'] = True
            self.response['butr'] = True
            self.response['dish'] = True
        elif x == 4:
            self.response['butr'] = True
            self.response['dish'] = True
        else:
            self.response['butr'] = True
            
        return 0
