"""
File: Asset.py
Description: This module contains Asset class and is used within rig.py and hacker.py for creating assets
Author: Tayla Fontanabella
ID: Fonty005
Username: taylaf001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# Asset Class
class Asset:
    def __init__(self, name, description, encrypted):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    # Getters for attributes
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    # Setters for attributes
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    def __str__(self): # String conversion method
        if self.__encrypted == True:
            return f"{self.__name}: {self.__description} - [Encrypted]"
        else:
            return f"{self.__name}: {self.__description} - [Decrypted]"

