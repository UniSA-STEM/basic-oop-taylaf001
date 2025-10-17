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
                    self.get_inventory().remove(Asset)
                    self.get_rig().upgrade()
                    return print("Hardware Patch detected in inventory.\n")
                else:
                    return print("Hardware Patch not found in inventory. Cannot upgrade.\n")
        else:
            return print("You have no rig. Cannot upgrade.\n")


    # Method for launching an attack with data spikes

    def launchAttack (self, targetRig):
        if self.get_exposure() == False: # Check if exposed
            if self.get_rig():
                for asset in self.get_rig().get_storage():
                    if asset.get_name() == "Data Spike":
                        self.get_rig().get_storage().remove(asset)
                        targetRig.damageCounter()
                        self.set_traceLevel(self.get_traceLevel()+1)
                        return print("Attack successful.")
            else:
                return print("\nYou have no rig to launch an attack with\n")
        else:
            return print(f"\nYou are exposed. You cannot launch an attack until you reduce your trace. Current Trace Level: {self.get_traceLevel()}\n")


    # Method for encrypting asset in either inventory or rig storage

    def encryptAsset(self, asset, rigOrHacker):
        securityChip = False
        securityChipInInventory = False
        securityChipInRig = False

        # Check for security Chip in hacker inventory
        for Asset in self.get_inventory():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                securityChipInInventory = True
                self.get_inventory().remove(Asset)

        # Check for security chip in rig storage, if rig is true
        if self.get_rig(): # Check for rig
            for Asset in self.get_rig().get_storage():
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
            print("\nSecurity Chip not found in rig storage or hacker inventory. Cannot encrypt.\n")


        # Encrypt asset in hackers inventory
        if securityChip == True and rigOrHacker == "Hacker":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset.get_name:
                    Asset.set_encrypted(True)
                    return print(f"Encryption Successful.\n{Asset.__str__()}\n")

        # Encrypt asset in rig storage
        elif securityChip == True and rigOrHacker == "Rig":
            if self.get_rig(): # Check for rig
                for Asset in self.get_rig().get_storage():
                    if Asset.get_name() == asset.get_name():
                        Asset.set_encrypted(True)
                        return print(f"Encryption Successful.\n{Asset.__str__()}\n")
                if asset.get_name() not in self.get_rig().get_storage():
                    print("Asset not found in rig storage or hacker inventory.\n")

            else:
                print("You have no rig.\n")


    # Method for decrypting asset in either inventory or rig storage

    def decryptAsset (self, asset, rigOrHacker):
        securityChip = False
        securityChipInInventory = False
        securityChipInRig = False

        # Check for security Chip in hacker inventory
        for Asset in self.get_inventory():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                securityChipInInventory = True
                self.get_inventory().remove(Asset)

        # Check for security chip in rig storage, if rig is true
        if self.get_rig():  # Check for rig
            for Asset in self.get_rig().get_storage():
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

        # Decrypt asset in hackers inventory
        if securityChip == True and rigOrHacker == "Hacker":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset.get_name:
                    Asset.set_encrypted(False)
                    return print(f"Decryption Successful.\n{Asset.__str__()}\n")

        # Decrypt asset in rig storage
        elif securityChip == True and rigOrHacker == "Rig":
            if self.get_rig():  # Check for rig
                for Asset in self.get_rig().get_storage():
                    if Asset.get_name() == asset.get_name():
                        Asset.set_encrypted(False)
                        return print(f"Decryption Successful.\n{Asset.__str__()}\n")
                if asset.get_name() not in self.get_rig().get_storage():
                    print("Asset not found in rig storage or hacker inventory.\n")

            else:
                print("You have no rig.\n")



    # Method for scanning for an asset and removing if found

    def assetRemovalScan(self, asset):
        for Asset in self.get_inventory():
            if Asset.get_name() == asset:
                self.get_inventory().remove(Asset)
                return print("Asset found. Removing Asset.\n")


    # Method for asset transfer

    def assetTransfer(self, asset, transferDestination):
        assetStorageRig = self.get_rig().get_storage()
        assetStorageHacker = self.get_inventory()
        self.set_traceLevel(self.get_traceLevel() + 1)

        # Transfer all to rig

        if transferDestination == "Rig" and asset == "All":
            for Asset in self.get_inventory():
                    self.get_inventory().remove(Asset)
                    assetStorageRig.append(Asset)
                    self.get_rig().set_storage(assetStorage)


        # Transfer asset to rig

        elif transferDestination == "Rig" and asset != "All":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    self.get_inventory().remove(Asset)
                    assetStorageRig.append(Asset)
                    self.get_rig().set_storage(assetStorage)

        # Transfer all to Hacker

        elif transferDestination == "Hacker" and asset == "All":
            for Asset in self.get_rig().get_storage():
                self.get_rig().get_storage().remove(Asset)
                assetStorageHacker.append(Asset)
                self.set_inventory(assetStorage)


        # Transfer asset to Hacker

        elif transferDestination == "Hacker" and asset != "All":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    self.get_rig().get_storage().remove(Asset)
                    assetStorageHacker.append(Asset)
                    self.set_inventory(assetStorage)

        else:
            print("Transfer destination must be Hacker or Rig.\n")


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

        return f"---------------\nName: {self.get_name()} \nRig Name: {rigName} \nTrace Level: {self.get_traceLevel()} \n--------------- \nInventory Contents: \n-- \n{assetStr} "