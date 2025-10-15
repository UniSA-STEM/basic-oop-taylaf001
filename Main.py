"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


# Function to ensure assets attributes are stored and displayed correctly in asset.py

def assetTest():
    asset = Asset("CryptoToken", "Test", False)
    print(asset)

# Function to ensure attributes are stored and displayed correctly in rig.py

def rigAttributeTest():
    print(rig)

# Function to test rig.py upgrade method

def rigUpgradeTest():
    hardwarePatch = Asset("Hardware Patch", "Used to upgrade rigs.", False)

    rig.storeAsset(hardwarePatch)
    rig.upgrade(hardwarePatch)

    print(f"Upgrade Level: {rig.get_upgradeLevel()}")
    print(f"Storage Amount: {rig.get_assetStorageAmount()}")

# Function to test asset generation method in rig.py

def assetGenerationTest():
    for asset in rig.get_storage():
        print(asset)
    print("\n")
    rig.assetGeneration()
    for asset in rig.get_storage():
        print(asset)

# Function to test damage counter method in rig.py

def damageCounterTest():
    rig.damageCounter()
    i = 1
    while i < 3:
        print(f"Damage Increment: {rig.get_damageCounter()}")
        print(f"Broken State: {rig.get_brokenState()}")
        print(f"Upgrade Level: {rig.get_upgradeLevel()}")
        print("\n")
        rig.damageCounter()
        i += 1

# Function to test repairing rig

def repairTest():
    asset = Asset("CryptoToken", "Test", False)
    rig.repair(asset)

# Function to test asset storing

def assetStorageTest():
    for asset in rig.get_storage():
        print(asset)
    print("\n")
    asset = Asset("CryptoToken", "Test", False)
    rig.storeAsset(asset)
    for asset in rig.get_storage():
        print(asset)

# Function to test removing/releasing assets

def releaseAssetTest():
    for asset in rig.get_storage():
        print(asset)
    print("\n")
    asset = Asset("Data Spike", "Used in Battles", True)
    rig.releaseAsset(asset)
    for asset in rig.get_storage():
        print(asset)

# Function to test display and result of rig condition method

def rigConditionTest():
    print(f"{rig.condition()}")

# Function to test string conversion method

def conversionTest():
    print(rig.__str__())

rig = Rig()


