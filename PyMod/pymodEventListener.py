
import threading
import os
import sys
import json

from .pymodErrors import *
from colorama import Fore, Back, Style,init
init()

class PyModListener:
    
    def __init__(self, path):
        self.path = path
        self.curData = self.load_data()
        self.run_thread = True
    
    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except Exception as e:
            print(e)


    def listener(self):
        while self.run_thread:
            if self.curData != self.load_data():
                fileNamePrint = f"{Fore.YELLOW}'{self.path}'{Style.RESET_ALL}"
                message = Fore.GREEN
                message += f"Found Changes in {fileNamePrint} {Fore.GREEN}File{Style.RESET_ALL}"
                message += Style.RESET_ALL
                print(message)
                self.curData = self.load_data()
                return True

    

    def run(self):
        self.run_thread = True
        self.run_thread = threading.Thread(target=self.listener)
        self.run_thread.start()
    

