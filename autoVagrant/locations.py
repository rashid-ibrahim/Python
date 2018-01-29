########################################################################################################
# Name: Required Include class for autostart.pyu and autostop.py                                       #
# Purpose: Loads the location of the grunt machines into getters and setters                           #
# Author: Rashid 'Lee' Ibrahim                                                                         #
# Date: 11/12/2017                                                                                     #
########################################################################################################

class locations:
    def __init__(self):
        self.butr = 'C:\GitHub\\butr'
        self.dish = 'C:\GitHub\\dish'
        self.gala = 'D:\GALA_Dev'

    def getButr(self):
        return self.butr

    def getDish(self):
        return self.dish

    def getGala(self):
        return  self.gala
