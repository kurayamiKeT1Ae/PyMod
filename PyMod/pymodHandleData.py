import threading
import os
import sys
import json
import asyncio

from .pymodErrors import *
from colorama import Fore, Back, Style,init

class PyModHandleData:

    def __init__(self, path):
        self.path = path
        

    def load_data(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except:
            return None


    async def _handle(self):
        ## handle data variables
        data = self.load_data()
        DIR = os.path.abspath(os.path.curdir)
        # print(data)
        data['__dir__'] = data['__dir__'].replace("${__dir__}", DIR)
        return data


