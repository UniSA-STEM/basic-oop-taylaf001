"""
File: Rig.py
Description: This python module represents a 'rig'. It includes a class and various private attributes utilised by the hacker class.
Author: Tayla Fontanabella
ID: Fonty005
Username: taylaf001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from Asset import Asset

# Rig Class
class Rig:
    def __init__(self):
        self.__name = "Rigger"
        self.__damageCounter = 0
        self.__brokenState = False
        self.__upgradeLevel = 0
        self.__assetStorageAmount = 3
        self.__storage = [Asset("Data Spike", "Used in Battles", False), Asset("Data Spike", "Used in Battles", False), Asset("Removable Drive", "Found in rigs and used for extraction", False)]

    # Getters for private attributes

    def get_name(self):
        return self.__name

    def get_damageCounter(self):
        return self.__damageCounter

    def get_brokenState(self):
        return self.__brokenState

    def get_upgradeLevel(self):
        return self.__upgradeLevel

    def get_assetStorageAmount(self):
        return self.__assetStorageAmount

    def get_storage(self):
        return self.__storage

    # Setters for private attributes

    def set_name(self, name):
        self.__name = name

    def set_damageCounter(self, damageCounter):
        self.__damageCounter = damageCounter

    def set_brokenState(self, brokenState):
        self.__brokenState = brokenState

    def set_upgradeLevel(self, upgradeLevel):
        self.__upgradeLevel = upgradeLevel

    def set_assetStorageAmount(self, assetStorageAmount):
        self.__assetStorageAmount = assetStorageAmount

    def set_storage(self, storage):
        self.__storage = storage

    # Rig Upgrade Method

    def upgrade(self):
        self.set_upgradeLevel(self.get_upgradeLevel() + 1)
        self.set_assetStorageAmount(self.get_assetStorageAmount() + 1)
        print(f"{self.get_name()} upgraded to level {self.get_upgradeLevel()}")
        return

    # Rig random asset generation method
    def assetGeneration(self):
        assetPossibilities = [Asset("Hardware Patch", "Used to upgrade rigs.", False), Asset("Removable Drive", "Used in rigs and used for extraction", False), Asset("Data Spike", "Used in rigs and used for extraction", False), Asset("CryptoToken", "Used to acquire or repair rigs", False), Asset("Security Chip", "Used to encrypt or decrypt assets.", False)]
        randomAsset = random.choice(assetPossibilities)
        self.get_storage().append(randomAsset)
        print(f"Asset Generated: {randomAsset.get_name()}")

    # Rig Takes Damage Method

    def damageCounter(self):
        self.set_damageCounter(self.get_damageCounter() + 1)
        if self.get_damageCounter() == 2 and self.get_upgradeLevel() == 0:
            self.set_brokenState(True)

    # Method to repair rig

    def repair(self, asset):
        if self.get_damageCounter() > 0 and asset.get_name() == "CryptoToken":
            self.set_damageCounter(0)
            self.set_brokenState(False)
            print("Repair Successful.")
        elif self.get_damageCounter() > 0 and asset.get_name() != "CryptoToken":
            print("No valid asset inputted.")
        else:
            print("No repair is needed.")

    # Method to store / add asset to rig

    def storeAsset(self, asset):
        assetStorage = self.get_storage()
        assetStorage.append(asset)
        self.set_storage(assetStorage)

    # Method releasing asset

    def releaseAsset(self, asset):
        for storedAsset in self.get_storage():
            if storedAsset.get_name() == asset.get_name() and asset.get_encrypted() == False:
                self.get_storage().remove(storedAsset)
                print("Asset released successfully.")
            elif storedAsset.get_name() == asset.get_name() and asset.get_encrypted() == True:
                print("Asset must be decrypted before transferring.")
            elif storedAsset.get_name() != asset.get_name():
                print("Asset not found in storage.")
            return

    # Method returning rig's condition

    def condition(self):
        conditionStr = ""
        if self.get_brokenState() == False:
            conditionStr = "Pristine"
        elif self.get_brokenState() == True:
            conditionStr = "Broken"
        return f"{conditionStr}(Level {self.get_upgradeLevel()})"

    # String Conversion Method

    def __str__(self):
        assetStr = ""
        for asset in self.get_storage():
            assetStr += str(asset) + "\n"
        return f"Name: {self.get_name()} \nCondition: {self.condition()} \nUpgrade Level: {self.get_upgradeLevel()} \n------ \nAssets: \n{assetStr} "
