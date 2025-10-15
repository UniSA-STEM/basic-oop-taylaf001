"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Tayla Fontanabella
ID: Fonty005
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

# Hacker Class
class Hacker:
    def __init__(self):
        self.__name = "Hackzilla"
        self.__traceLevel = 0
        self.__storage = [Asset("CryptoToken", "Used to acquire or repair rigs.", False)]
        self.__rig = False

    # Getters for private attributes

    def get_name(self):
        return self.__name

    def get_traceLevel(self):
        return self.__traceLevel

    def get_storage(self):
        return self.__storage

    def get_rig(self):
        return self.__rig

    # Setters for private attributes

    def set_name(self, name):
        self.__name = name

    def set_traceLevel(self, traceLevel):
        self.__traceLevel = traceLevel

    def set_storage(self, storage):
        self.__storage = storage

    def set_rig(self, rig):
        self.__rig = rig

    # Method for acquiring a rig

    def acquireRig(self, asset):


