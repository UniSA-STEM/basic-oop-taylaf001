"""
File: Asset.py
Description: <A brief description of this Python module.>
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

    # String conversion method
    def __str__(self):
        if self.__encrypted == True:
            return f"{self.__name}: {self.__description}[Encrypted]"
        else:
            return f"{self.__name}: {self.__description}"

