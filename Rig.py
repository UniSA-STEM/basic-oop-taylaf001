"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self):
        self.__name = "Rigger"
        self.__damageCounter = 0
        self.__brokenState = False
        self.__upgradeLevel = 0
    
    def storage(self):
        self.dataSpikes = 2
        self.removableDrive = 1
    
    def repair(self):
        if damageCounter > 0:
            self.__damageCounter = 0
            self.brokenState = False
        else:
            print("No repair is needed.")
    
