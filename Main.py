"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import asset

from Asset import Asset
from Rig import Rig
from Hacker import Hacker

def assetTest(): # Function to ensure assets attributes are stored and displayed correctly in asset.py
    asset = Asset("CryptoToken", "Test", False)
    print(asset)

def rigUpgradeTest(): # Individual testing of rig upgrade (no hacker involvement)
    hardwarePatch = Asset("Hardware Patch", "Used to upgrade rigs.", False)

    rig.storeAsset(hardwarePatch)
    rig.upgrade(hardwarePatch)

    print(f"Upgrade Level: {rig.get_upgradeLevel()}")
    print(f"Storage Amount: {rig.get_assetStorageAmount()}")

def assetGenerationTest(): # Function to test asset generation method in rig.py
    for asset in rig.get_storage():
        print(asset)
    print("\n")
    rig.assetGeneration()
    for asset in rig.get_storage():
        print(asset)

def damageCounterTest(): # Function to test damage counter method in rig.py
    rig.damageCounter()
    i = 1
    while i < 3:
        print(f"Damage Increment: {rig.get_damageCounter()}")
        print(f"Broken State: {rig.get_brokenState()}")
        print(f"Upgrade Level: {rig.get_upgradeLevel()}")
        print("\n")
        rig.damageCounter()
        i += 1

def repairTest(): # Function to test repairing rig
    asset = Asset("CryptoToken", "Test", False)
    rig.repair(asset)

def assetStorageTest(): # Function to test asset storing
    for asset in rig.get_storage():
        print(asset)
    print("\n")
    asset = Asset("CryptoToken", "Test", False)
    rig.storeAsset(asset)
    for asset in rig.get_storage():
        print(asset)

def releaseAssetTest(): # Function to test releasing assets to hackers inventory (encryption test included)
    print("Assets in Rig Storage: \n")
    for asset in rig.get_storage(): # Check initial rig storage
        print(asset)
    print("\n")
    asset = Asset("Data Spike", "Used in Battles", True)
    rig.releaseAsset(asset, hacker)
    for asset in rig.get_storage(): # Check updated rig storage
        print(asset)
    print("\n")
    for asset in hacker.get_inventory(): # Check updated hacker storage
        print(asset)

def rigConditionTest(): # Function to test display and result of rig condition method
    print(f"{rig.condition()}")

def rigAttributeTest(): # Function to test string conversion method for rig
    print(rig.__str__())

def hackerAttributeTest(): # Function to test string conversion method for hacker
    print(hacker.__str__())

def acquireRigTest(): # Function to test acquiring a rig
    hacker.acquireRig()

def upgradeRigTest(): # Function to test upgrading rig
    asset = Asset("Hardware Patch", "Used to upgrade rigs.", False)
    acquireRigTest()
    i = 0
    while i < 4:
        hacker.get_rig().assetGeneration()
        i += 1  # generates random assets to assist in testing if hardware patch = true, then rig upgrades
    hacker.get_rig().releaseAsset(asset, hacker)
    hacker.upgradeRig()

def encryptAssetTest(): # Encryption Test Function
    asset = Asset("CryptoToken", "Used to acquire or repair rigs.", False)
    rigOrHacker = "Rig"
    hackerAttributeTest() # Check initial hacker details
    acquireRigTest() # Acquire Rig
    hackerAttributeTest() # Check rig has been successfully acquired
    i = 0 #  generates random assets to assist in asset encryption provided a security chip is in storage
    while i < 5:
        hacker.get_rig().assetGeneration()
        i += 1
    hacker.encryptAsset(asset, rigOrHacker) # Check if encryption is successful

def decryptAssetTest(): # Asset decryption check
    asset = Asset("CryptoToken", "Used to acquire or repair rigs.", False)
    rigOrHacker = "Rig"
    hackerAttributeTest()  # Check initial hacker details
    acquireRigTest()  # Acquire Rig
    hackerAttributeTest()  # Check rig has been successfully acquired
    i = 0  # generates random assets to assist in asset encryption provided a security chip is in storage
    while i < 4:
        hacker.get_rig().assetGeneration()
        i += 1
    hacker.decryptAsset(asset, rigOrHacker)  # Check if encryption is successful

def assetTransferTest(): # Asset transfer between both rig storage and hacker inventory
    hacker.acquireRig()
    assetToTransfer = Asset("CryptoToken", "Used to transfer assets.", False)
    hacker.get_inventory().append(assetToTransfer)
    print("TRANSFER TEST 1 (Hacker to Rig)")
    print("---------")
    print("Hacker Inventory:")
    for asset in hacker.get_inventory():
        print(asset)
    print("---------")
    print("Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset)
    print("---------")
    hacker.assetTransfer(assetToTransfer, "Rig")
    print("---------")
    print("Updated Hacker Inventory:")
    for asset in hacker.get_inventory():
        print(asset)
    print("---------")
    print("Updated Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset)
    print("---------")
    print("TRANSFER TEST 2 (Rig to Hacker)")
    print("---------")
    print("Hacker Inventory:")
    for asset in hacker.get_inventory():
        print(asset)
    print("---------")
    print("Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset)
    print("---------")
    hacker.assetTransfer(assetToTransfer, "Hacker")
    print("---------")
    print("Updated Hacker Inventory:")
    for asset in hacker.get_inventory():
        print(asset)
    print("---------")
    print("Updated Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset)
    print("---------")


def assetRemovalScanTest(): # Testing method to scan for an asset in hacker inventory and remove if found
    print("------------")
    print("Hacker Inventory:")
    for asset in hacker.get_inventory():
        print(asset)
    print("------------")
    asset = Asset("CryptoToken", "Used to acquire or repair rigs.", False)
    hacker.assetRemovalScan(asset)
    print("------------")
    print("Updated Hacker Inventory:")
    print("------------")
    for asset in hacker.get_inventory():
        print(asset)



def launchFullAttackTest(): # Testing a full attack including giving the hacker rig extra assets, upgrading rig to test all conditions and response when increasing trace level
    attackNo = 1
    enemy = Hacker()
    enemy.set_name("Enemy")
    hacker = Hacker()
    enemy.acquireRig()
    hacker.acquireRig()

    print(enemy.__str__())
    print(hacker.__str__())

    print("----------------------------")
    print("Current Hacker Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    print("----------------------------")
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    hacker.get_rig().get_storage().append(Asset("Removable Drive", "Used in Battles", False))
    attackNo += 1
    print("----------------------------")
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    print("----------------------------")
    attackNo += 1
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    print("----------------------------")
    attackNo += 1
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")
    i = 0
    while i < 2:
        hacker.get_rig().get_storage().append(Asset("Data Spike", "Used in Battles", False))
        i += 1
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    print("----------------------------")
    attackNo += 1
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")
    for asset in hacker.get_rig().get_storage():
        print(asset.get_name())
    print("----------------------------")
    attackNo += 1
    print(f"Launching attack {attackNo} on enemy rig\n")
    hacker.launchAttack(enemy.get_rig())

    print("----------------------------")
    print("Updated Hacker Rig Storage:")

    print(enemy.__str__())
    print(hacker.__str__())


rig = Rig()
hacker = Hacker()










