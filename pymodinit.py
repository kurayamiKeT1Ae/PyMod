

import os

VERSION = "0.0.2"

CODE = """

@echo off

py pymodrun.py %1

"""

def init():
    with open("pymod.bat", 'w') as file:
        file.writelines(CODE)


init()