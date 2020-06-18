#code:utf-8

import datetime
import math
import numpy as np
from settings import *


class Step_type():
  
    def __init__(self, step_id, description, employee_skill, equipment_type, duration, quantity_per_batch):
        self.step_id = step_id 
        self.description = description
        self.employee_skill = employee_skill
        self.equipment_type = equipment_type
        self.duration_intervalle = math.ceil(duration / INTERVALLE)
        # self.quantity_per_batch = quantity_per_batch


    def show(self):
        print(f"Step ID : {self.step_id} \nDescription : {self.description} \nEmployee skill : {self.employee_skill} \nEquipment type : {self.equipment_type} \nDuration in minutes : {self.duration} \nQuantity per batch : {self.quantity_per_batch}")
