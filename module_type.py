#code:utf-8

import datetime
import numpy as np
from mfg_step import Mfg_step


class Module_type():
  
    def __init__(self, module_type_id):
        self.module_type_id = module_type_id 
        self.steps = []
    

    def show(self):
        print(f"The manucturing steps of the module type '{self.module_type_id}'  are :")
        for step in self.steps:
            step.show()


    def add_step(self, step_type, step_number=1000):
        mfg_step = Mfg_step(step_type, step_number)
        for step in self.steps:
            if mfg_step.step_number == step.step_number:
                for step in self.steps:
                    if step.step_number >= mfg_step.step_number:
                        step.step_number += 1
                break
        if mfg_step.step_number > len(self.steps) + 1:
           mfg_step.step_number = len(self.steps) + 1     
        self.steps.append(mfg_step)
        self.steps = sorted(self.steps, key=lambda mfg_stp: mfg_stp.step_number)  