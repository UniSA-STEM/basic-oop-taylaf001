"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description, encrypted):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        self.conversion = ""
        if self.__encrypted == True:
            self.conversion = (f"{self.__name}:{self.__description} [Encrypted]")
        elif self.__encrypted == False:
            self.conversion = (f"{self.__name}:{self.__description}")
        elif self.__encrypted == "":
            self.conversion = (f"{self.__name}:{self.__description}")

        return self.conversion