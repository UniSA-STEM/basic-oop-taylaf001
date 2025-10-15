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
    asset = Asset("CrypoToken", "Test", True)
    print(asset)

# Function to ensure attributes are stored and displayed correctly in rig.py
def rigAttributeTest():
    print(rig)

# Function to test rig.py upgrade method
def rigUpgradeTest():
    hardwarePatch = Asset("Hardware Patch", "Used to upgrade rigs.", False)

    rig.storeAsset(hardwarePatch)
    rig.upgrade(hardwarePatch)

    print(rig.get_upgradeLevel())
    print(rig.get_assetStorageAmount())

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
    i = 1
    while i < 3:
        print(f"Damage Increment: {rig.get_damageCounter()}")
        print(f"Broken State: {rig.get_brokenState()}")
        print(f"Upgrade Level: {rig.get_upgradeLevel()}")
        print("\n")
        rig.damageCounter()
        i += 1

rig = Rig()
rigUpgradeTest()
damageCounterTest()