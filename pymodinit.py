

import os

CODE = """

@echo off

py pymodrun.py %1

"""

def init():
    with open("pymodrun.bat", 'w') as file:
        file.writelines(CODE)


init()