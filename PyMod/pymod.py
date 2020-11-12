import os
import sys
import json


## get vars
from . import ABS_PATH, PYMOD_PKG, PYMOD_INIT_DATA

## get error classes
from .pymodErrors import *
## get file eventlistener
from .pymodEventListener import PyModListener

class PyMod:

    def __init__(self, sys):
        self.sys_run_command = sys.argv[1] ## get the run command
        self._data = self.load_data() ## get json data
        self.filename = self._data['run'][self.sys_run_command].split(" ")[1] ## get filename
        self.Listener = PyModListener(self.filename) ## listening to the file


    def load_data(self):
        """
        TODO: loading data from the pymodPKG.json file
        """
        try:
            with open(PYMOD_INIT_DATA, 'r') as file:
                return json.load(file)
        except:
            raise LoadPyModPKGError(f"Can't Open {PYMOD_INIT_DATA} file")


    def _THREAD(self, run_command):
        """
        TODO: make a thread and listen to the file
        """
        while True:
            if self.Listener.listener():
                try:
                    os.system(run_command)
                except Exception as e:
                    print(e)
            

    def run(self):
        """
        TODO: run the code
        """
        run_command = None
        try:
            run_command = self.load_data()['run'][self.sys_run_command]
        except:
            raise RunCommandNotFound(f"command: {self.sys_run_command} not found in the pymodPKG.json file > [run] commands")

        try:
            os.system(run_command)
        except:
            pass

        while True:
            self._THREAD(run_command)

       