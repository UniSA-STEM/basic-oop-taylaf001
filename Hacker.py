"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Tayla Fontanabella
ID: Fonty005
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

# Hacker Class
class Hacker:
    def __init__(self):
        self.__name = "Hackzilla"
        self.__traceLevel = 0
        self.__traceThreshold = 5
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.", False)]
        self.__rig = False
        self.__exposure = False

    # Getters for private attributes

    def get_name(self):
        return self.__name

    def get_traceLevel(self):
        return self.__traceLevel

    def get_traceThreshold(self):
        return self.__traceThreshold

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_exposure(self):
        return self.__exposure

    # Setters for private attributes

    def set_name(self, name):
        self.__name = name

    def set_traceLevel(self, traceLevel):
        self.__traceLevel = traceLevel

    def set_traceThreshold(self, traceThreshold):
        self.__traceThreshold = traceThreshold

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_rig(self, rig):
        self.__rig = rig

    def set_exposure(self, exposure):
        self.__exposure = exposure

    # Method for acquiring a rig

    def acquireRig(self, asset):
        if self.get_rig() == False:
            for storedAsset in self.get_inventory():
                if storedAsset.get_name() == asset.get_name() and asset.get_name() == "CryptoToken":
                    self.get_inventory().remove(asset)
                    self.set_rig(Rig)
                    print("Rig Acquired and Activated")
                    return
                else:
                    print("CryptoToken not found in your inventory")
        else:
            print("You have a rig. Cannot acquire a second rig.")

    # Method for launching an attack with data spikes

    def launchAttack (self, targetRig):
        if self.get_exposure() == False:
            if self.get_rig():
                # Put in remove asset here - need to develop other methods first
                targetRig.damageCounter()
                self.set_traceLevel(self.get_traceLevel()+1)
            else:
                print("You have no rig to launch an attack with")
                return
        else:
            print(f"You are exposed. You cannot launch an attack until you reduce your trace. Current Trace Level: {self.get_traceLevel()}")

    # Method for encrypting asset in either inventory or rig storage

    def encryptAsset(self, asset, rigOrHacker):
        rigOrHacker = rigOrHacker
        if rigOrHacker == "Hacker":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(True)
                else:
                    print("Asset not found in inventory")
                return
        elif rigOrHacker == "Rig":
            Rig = self.get_rig()
            for Asset in Rig.get_storage():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(True)
                else:
                    print("Asset not found in storage")



    # Method for decrypting asset in either inventory or rig storage

    def decryptAsset (self, asset):

    # Method for transferring assets from inventory to rig storage and vice versa

    def transferToStorage (self, asset):

    # Method for retrieving assets from rig storage or inventory or vice versa

    def retrieveFromStorage (self, asset):

    # String Conversion Method

    def __str__(self):
        assetStr = ""
        for asset in self.get_inventory():
            assetStr += str(asset) + "\n"
        return f"Name: {self.get_name()} \nRig Name: {rig.get_name()} \nTrace Level: {self.get_traceLevel()} \n------ \nInventory Contents: \n{assetStr} "