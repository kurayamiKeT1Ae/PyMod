
import threading
import os
import sys
import json
import asyncio

from .pymodErrors import *
from . import PYMOD_INIT_DATA
from .pymodHandleData import PyModHandleData
from colorama import Fore, Back, Style,init
init()

class PyModListener:
    
    def __init__(self, path):
        self.path = path
        self.DATA_PATH = PYMOD_INIT_DATA
        # print(self.curdir)
        self.pymodHandleData = PyModHandleData(self.DATA_PATH)
        # self.curData = self.load_data()
        self.curData = {}
        self.run_thread = True
    

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except Exception as e:
            print(e)
            return None

    def load_file(self, file):
        try:
            with open(file, 'r') as file:
                return file.read()
        except:
            return None

    def init_curData(self):
        DATA = asyncio.run(self.pymodHandleData._handle()) ## handle data
        dirFiles = os.listdir(DATA['__dir__']) # get list of dir files
        dirFiles = [file for file in dirFiles if os.path.isfile(file)] # get files only without dirs
        DIR = {filename: self.load_file(filename) for filename in dirFiles if filename not in (DATA['ignore'])} ## handle files data and ignore ["ignore"] files
        return DIR ## return the data


    def listener(self):
        ## listen to changes
        self.curData = self.init_curData() 
        while self.run_thread:
            for filename in self.curData:
                if self.curData[filename] != self.load_file(filename):
                    fileNamePrint = f"{Fore.YELLOW}'{filename}'{Style.RESET_ALL}"
                    message = Fore.GREEN
                    message += f"Found Changes in {fileNamePrint} {Fore.GREEN}File{Style.RESET_ALL}"
                    message += Style.RESET_ALL
                    print(message)
                    self.curData[filename] = self.load_file(filename)
                    return True

    

    def run(self):
        self.run_thread = True
        self.run_thread = threading.Thread(target=self.listener)
        self.run_thread.start()
    

