#code:utf-8

import datetime
import numpy as np
from step_type import Step_type

class Mfg_step():
    
    def __init__(self, step_type, step_number):
        self.step_type = step_type 
        self.step_number = step_number

    def show(self):
        print(f"The step {self.step_number} of the manufacturing process has the following features :")
        self.step_type.show()
    
    def __repr__(self):
        return repr((self.type, self.number))