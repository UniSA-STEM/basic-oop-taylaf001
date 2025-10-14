"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
# Rig Class
class Rig:
    def __init__(self):
        self.__name = "Rigger"
        self.__damageCounter = 0
        self.__brokenState = False
        self.__upgradeLevel = 0
        self.__assetStorageAmount = 3
        self.__storage = [Asset("Data Spike", "Used in Battles", False), Asset("Data Spike", "Used in Battles", False), Asset("Removable Drive", "Found in rigs and used for extraction", False)]


    # Rig Upgrade Method
    def upgrade(self, asset):
        if asset.name == "Hardware Patch":
            self.__storage.remove(asset)
            self.__upgradeLevel += 1
            self.__assetStorageAmount += 1

    # Rig asset generation method
    def assetGeneration(self):


    # Rig Takes Damage Method
    def damageCounter(self):
        self.__damageCounter += 1
        if self.__damageCounter == 2 and self.__upgradeLevel == 0:
            self.__brokenState = True

    # Method to repair rig
    def repair(self):
        if self.__damageCounter > 0:
            self.__damageCounter = 0
            self.brokenState = False
        else:
            print("No repair is needed.")

    # Method to store / add asset to rig
    def storeAsset(self, asset):
        self.__storage.append(asset)

    # Method releasing asset
    def releaseAsset(self, asset):
        if asset in self.__storage:
            self.__storage.remove(asset)
        else:
            print("No asset in rig storage.")

    # Method returning rig's condition
    def condition(self):
        self.conditionStr = ""
        if self.__brokenState == False:
            self.conditionStr = "Pristine"
        elif self.__brokenState == True:
            self.conditionStr = "Broken"

        return f"{self.conditionStr} ({self.__upgradeLevel})"

    # String Conversion Method
    def __str__(self)
        return f"{self.__name}, {self.}
