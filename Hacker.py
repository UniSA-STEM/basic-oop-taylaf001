"""
File: Hacker.py
Description: Hacker.py contains a hacker class which is utilised within a game.
Author: Tayla Fontanabella
ID: Fonty005
Username: Taylaf001
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

    # Method for acquiring a rig

    def acquireRig(self):
        if self.get_rig() == False:
            for asset in self.get_inventory():
                if asset.get_name() == "CryptoToken":
                    self.get_inventory().remove(asset)
                    self.set_rig(Rig())
                    return print("Rig Acquired and Activated.\n")
                else:
                    return print("CryptoToken not found in your inventory.\n")
        else:
            return print("You have a rig. Cannot acquire a second rig.\n")

    # Method for upgrading rig

    def upgradeRig(self):
        hardwarePatch = False
        if self.get_rig(): # Check for rig
            for Asset in self.get_inventory():
                if Asset.get_name() == "Hardware Patch":
                    hardwarePatch = True
                    print("Hardware Patch detected in inventory.\n")
                    self.get_inventory().remove(Asset)
                    return self.get_rig().upgrade()

        else:
            return print("You have no rig. Cannot upgrade.\n")

        if hardwarePatch == False:
            print("'Hardware Patch' not found in inventory. Cannot upgrade.\n")

    def launchAttack (self, targetRig): # Method for launching an attack with data spikes
        dataSpike = False
        removableDrive = False
        if self.get_traceLevel() < self.get_traceThreshold(): # Check if exposed
            if self.get_rig(): # Check if rig has been acquired
                for asset in self.get_rig().get_storage():
                    if asset.get_name() == "Data Spike":
                        dataSpike = True
                        self.get_rig().get_storage().remove(asset)
                        targetRig.damageCounter()
                        self.set_traceLevel(self.get_traceLevel()+1)
                        print("Attack successful.\n")
                if dataSpike == False: # If no data spike, cannot launch attack
                    return print("No Data Spike detected. Cannot launch attack.\n")

            else:
                return print("You have no rig to launch an attack with.\n")

            for asset in self.get_rig().get_storage(): # Check if removable drive in storage for asset extraction process
                if asset.get_name() == "Removable Drive":
                    removableDrive = True

            if removableDrive == True:
                print("Removable Drive detected. Proceeding to assess condition of enemy rig.\n")

            if removableDrive == False:
                return print("No Removable Drive detected. Unable to extract assets from enemy rig.\n")

            if targetRig.get_brokenState() == True and removableDrive == True: # Extract unsecure assets from enemy/target rig
                for asset in self.get_rig().get_storage():  # Check if removable drive in storage for asset extraction process
                    if asset.get_name() == "Removable Drive":
                        self.get_rig().get_storage().remove(asset)
                print(f"Enemy Rig Broken. Proceeding to extract unsecure assets...\n")
                for asset in targetRig.get_storage():
                    if asset.get_encrypted() == False:
                        targetRig.get_storage().remove(asset)
                        self.get_rig().get_storage().append(asset)
                        print(f"'{asset.get_name()}' successfully extracted from enemy rig.\n")
                    else:
                        print(f"'{asset.get_name()}' unsuccessfully extracted due to encryption.\n")
            elif targetRig.get_brokenState() == False and removableDrive == True:
                print("Enemy rig not broken. Cannot proceed to extract unsecured assets.\n")

        else:
            return print(f"You are exposed. You cannot launch an attack until you reduce your trace. Current Trace Level: {self.get_traceLevel()}\n")

    def encryptAsset(self, asset, rigOrHacker): # Method for encrypting asset in either inventory or rig storage
        securityChip = False
        securityChipInInventory = False
        securityChipInRig = False

        for Asset in self.get_inventory(): # Check for security Chip in hacker inventory
            if Asset.get_name() == "Security Chip":
                securityChip = True
                securityChipInInventory = True
                self.get_inventory().remove(Asset)

        if self.get_rig(): # Check for rig
            for Asset in self.get_rig().get_storage(): # Check for security chip in rig storage, if rig is true
                if Asset.get_name() == "Security Chip":
                    securityChip = True
                    securityChipInRig = True
                    self.get_rig().get_storage().remove(Asset)
        else:
            print("You have no rig.\n")

        if securityChipInInventory == True:
            print(f"Security Chip detected in hacker inventory. Proceeding to asset detection\n")
        elif securityChipInRig == True:
            print(f"Security Chip detected in rig storage. Proceeding to asset detection.\n")

        if securityChip == False:
            print("Security Chip not found in rig storage or hacker inventory. Cannot encrypt.\n")


        if securityChip == True and rigOrHacker == "Hacker": # Encrypt asset in hacker's inventory
            for Asset in self.get_inventory():
                if Asset.get_name() == asset.get_name:
                    Asset.set_encrypted(True)
                    return print(f"Encryption Successful.\n{Asset.__str__()}\n")

        elif securityChip == True and rigOrHacker == "Rig": # Encrypt asset in rig storage
            if self.get_rig(): # Check for rig
                for Asset in self.get_rig().get_storage():
                    if Asset.get_name() == asset.get_name():
                        Asset.set_encrypted(True)
                        return print(f"Encryption Successful.\n{Asset.__str__()}\n")
                if asset.get_name() not in self.get_rig().get_storage():
                    print("Asset not found in rig storage or hacker inventory.\n")

            else:
                print("You have no rig.\n")

    def decryptAsset (self, asset, rigOrHacker): # Method for decrypting asset in either inventory or rig storage
        securityChip = False
        securityChipInInventory = False
        securityChipInRig = False

        for Asset in self.get_inventory(): # Check for security Chip in hacker inventory
            if Asset.get_name() == "Security Chip":
                securityChip = True
                securityChipInInventory = True
                self.get_inventory().remove(Asset)

        if self.get_rig():  # Check for rig
            for Asset in self.get_rig().get_storage(): # Check for security chip in rig storage, if rig is true
                if Asset.get_name() == "Security Chip":
                    securityChip = True
                    securityChipInRig = True
                    self.get_rig().get_storage().remove(Asset)
        else:
            print("\nYou have no rig.\n")

        if securityChipInInventory == True:
            print(f"\nSecurity Chip detected in hacker inventory. Proceeding to asset detection\n")
        elif securityChipInRig == True:
            print(f"\nSecurity Chip detected in rig storage. Proceeding to asset detection.\n")

        if securityChip == False:
            print("\nSecurity Chip not found in rig storage or hacker inventory. Cannot decrypt.\n")

        if securityChip == True and rigOrHacker == "Hacker": # Decrypt asset in hackers inventory
            for Asset in self.get_inventory():
                if Asset.get_name() == asset.get_name:
                    Asset.set_encrypted(False)
                    return print(f"Decryption Successful.\n{Asset.__str__()}\n")

        elif securityChip == True and rigOrHacker == "Rig": # Decrypt asset in rig storage
            if self.get_rig():
                for Asset in self.get_rig().get_storage():
                    if Asset.get_name() == asset.get_name():
                        Asset.set_encrypted(False)
                        return print(f"Decryption Successful.\n{Asset.__str__()}\n")
                if asset.get_name() not in self.get_rig().get_storage():
                    print("Asset not found in rig storage or hacker inventory.\n")

            else:
                print("You have no rig.\n")


    def assetRemovalScan(self, asset): # Method for scanning for an asset and removing if found
        for Asset in self.get_inventory():
            if Asset.get_name() == asset.get_name():
                self.get_inventory().remove(Asset)
                print(f"\nAsset '{Asset.get_name()}' found in inventory. Removing Asset.\n")

    def assetTransfer(self, asset, transferDestination):
        # Method for asset transfer
        self.set_traceLevel(self.get_traceLevel() + 1)
        if self.get_rig():
            if self.get_traceLevel() < self.get_traceThreshold():
                if transferDestination == "Rig" and asset == "All": # Transfer all to rig
                    for Asset in self.get_inventory():
                            self.get_inventory().remove(Asset)
                            self.get_rig().get_storage().append(Asset)
                            print(f"Asset '{Asset.get_name()}' transferred from Hacker to {transferDestination}")

                elif transferDestination == "Rig" and asset != "All": # Transfer asset to rig
                    for Asset in self.get_inventory():
                        if Asset.get_name() == asset.get_name():
                            self.get_inventory().remove(Asset)
                            self.get_rig().get_storage().append(Asset)
                            print(f"Asset '{Asset.get_name()}' transferred from Hacker to {transferDestination}")

                elif transferDestination == "Hacker" and asset == "All": # Transfer all to Hacker
                    for Asset in self.get_rig().get_storage():
                        self.get_rig().get_storage().remove(Asset)
                        self.get_inventory().append(Asset)
                        print(f"Asset '{Asset.get_name()}' transferred from Rig to {transferDestination}")

                elif transferDestination == "Hacker" and asset != "All": # Transfer asset to Hacker
                    for Asset in self.get_rig().get_storage():
                        if Asset.get_name() == asset.get_name():
                            self.get_rig().get_storage().remove(Asset)
                            self.get_inventory().append(Asset)
                            print(f"Asset '{Asset.get_name()}' transferred from Rig to '{transferDestination}'")

                else:
                    print("Transfer destination must be Hacker or Rig.\n")
            else:
                print("Trace Level exceeded threshold. You are exposed and need to reduce your trace level.\n")
        else:
            print("No rig available.\n")
    # String Conversion Method

    def __str__(self):
        assetStr = ""
        rigName = ""

        for asset in self.get_inventory():
            assetStr += str(asset) + "\n"

        if self.get_rig() != False:
            rigName = self.get_rig().get_name()
        else:
            rigName = "No rig in inventory."

        return f"---------------\nName: {self.get_name()} \nRig Name: {rigName} \nTrace Level: {self.get_traceLevel()} \n--------------- \nInventory Contents: \n{assetStr} "