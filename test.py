#!/usr/bin/python3
from controller import *

controller = Controller()       # Create the controller object from Controller class

while True:
        controller.update_state()
        controller.print_status()
        time.sleep(8)

