

import os
import sys

VERSION = "0.0.4"

CODE = """
@echo off
py pymodrun.py %1
"""

def init():
    filename = "pymod"
    try:
        filename = sys.argv[1]
    except:
        pass
    with open(f"{filename}.bat", 'w') as file:
        file.writelines(CODE)
    

init()