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
                    self.set_rig(Rig)
                    print("Rig Acquired and Activated")
                    return
                else:
                    print("CryptoToken not found in your inventory")
        else:
            print("You have a rig. Cannot acquire a second rig.")

    # Method for upgrading rig

    def upgradeRig(self):
        hardwarePatch = False
        if self.get_rig():
            Rig = self.get_rig()
            for Asset in self.get_inventory():
                if Asset.get_name() == "Hardware Patch":
                    hardwarePatch = True
                    print("Hardware Patch detected in inventory")
                    self.get_inventory().remove(Asset)
                    Rig.upgrade()
                else:
                    print("Hardware Patch not found in inventory. Cannot upgrade")
        else:
            print("You have no rig. Cannot upgrade.")


    # Method for launching an attack with data spikes

    def launchAttack (self, targetRig):
        if self.get_exposure() == False:
            if self.get_rig():
                for asset in self.get_rig().get_storage():
                    if asset.get_name() == " Data Spike":
                        targetRig.damageCounter()
                        self.set_traceLevel(self.get_traceLevel()+1)
                        print("Attack successful.")
            else:
                print("You have no rig to launch an attack with")
                return
        else:
            print(f"You are exposed. You cannot launch an attack until you reduce your trace. Current Trace Level: {self.get_traceLevel()}")

    # Method for encrypting asset in either inventory or rig storage

    def encryptAsset(self, asset, rigOrHacker):
        rigOrHacker = rigOrHacker
        securityChip = False

        # Check for security Chip

        for Asset in self.get_inventory():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                print("Security Chip detected in inventory")
                self.get_inventory().remove(Asset)
            else:
                print("Security Chip not found in inventory. Checking Rig.")
            return
        for Asset in self.get_rig().get_storage():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                print("Security Chip detected in storage")
                self.get_rig().get_storage().remove(Asset)
            else:
                print("Security Chip not found in storage or rig.")
            return

        # Encrypt asset depending on whether its in the hacker inventory or rig storage

        if securityChip == True and rigOrHacker == "Hacker":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(True)
                    print("Encryption Successful")
                else:
                    print("Asset not found in inventory")
                return
        elif securityChip == True and rigOrHacker == "Rig":
            for Asset in self.get_name().get_storage():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(True)
                    print("Encryption Successful")
                else:
                    print("Asset not found in storage")
                return

    # Method for decrypting asset in either inventory or rig storage

    def decryptAsset (self, asset, rigOrHacker):
        rigOrHacker = rigOrHacker
        securityChip = False

        # Check for security Chip
        for Asset in self.get_inventory():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                print("Security Chip detected in inventory")
                self.get_inventory().remove(Asset)
            else:
                print("Security Chip not found in inventory. Checking Rig.")
            return
        for Asset in self.get_rig().get_storage():
            if Asset.get_name() == "Security Chip":
                securityChip = True
                print("Security Chip detected in storage")
                self.get_rig().remove(Asset)
            else:
                print("Security Chip not found in storage or rig.")
            return

        # Decrypt asset depending on whether its in the hacker inventory or rig storage

        if securityChip == True and rigOrHacker == "Hacker":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(False)
                    print("Decryption Successful")
                else:
                    print("Asset not found in inventory")
                return
        elif securityChip == True and rigOrHacker == "Rig":
            for Asset in self.get_rig().get_storage():
                if Asset.get_name() == asset:
                    Asset.set_encrypted(False)
                    print("Decryption Successful")
                else:
                    print("Asset not found in storage")
                return


    # Method for scanning for an asset and removing if found

    def assetRemovalScan(self, asset):
        for Asset in self.get_inventory():
            if Asset.get_name() == asset:
                print("Asset found. Removing Asset.")
                self.get_inventory().remove(Asset)
            return

    # Method for
    def assetTransfer(self, asset, transferDestination):
        asset = asset
        transferDestination = transferDestination
        assetStorageRig = self.get_rig().get_storage()
        assetStorageHacker = self.get_inventory()
        # Transfer all to rig
        if transferDestination == "Rig" and asset == "All":
            for Asset in self.get_inventory():
                    self.get_inventory().remove(Asset)
                    assetStorageRig.append(Asset)
                    self.get_rig().set_storage(assetStorage)
            return
        # Transfer asset to rig
        elif transferDestination == "Rig" and asset != "All":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    self.get_inventory().remove(Asset)
                    assetStorageRig.append(Asset)
                    self.get_rig().set_storage(assetStorage)
            return
        # Transfer all to Hacker
        elif transferDestination == "Hacker" and asset == "All":
            for Asset in self.get_rig().get_storage():
                self.get_rig().get_storage().remove(Asset)
                assetStorageHacker.append(Asset)
                self.set_inventory(assetStorage)
            return

        # Transfer asset to Hacker
        elif transferDestination == "Hacker" and asset != "All":
            for Asset in self.get_inventory():
                if Asset.get_name() == asset:
                    self.get_rig().get_storage().remove(Asset)
                    assetStorageHacker.append(Asset)
                    self.set_inventory(assetStorage)
            return
        else:
            print("Transfer destination must be Hacker or Rig")


    # String Conversion Method

    def __str__(self):
        assetStr = ""
        for asset in self.get_inventory():
            assetStr += str(asset) + "\n"
        return f"Name: {self.get_name()} \nRig Name: {self.get_rig().get_name()} \nTrace Level: {self.get_traceLevel()} \n------ \nInventory Contents: \n{assetStr} "