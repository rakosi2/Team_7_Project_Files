#!/usr/bin/python3
from controller import *

controller = Controller()       # Create the controller object from Controller class

while True:
    for each_state in State:
        controller.update_state(each_state)
        # controller.print_status()
        time.sleep(1)
