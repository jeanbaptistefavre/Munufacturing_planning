#code:utf-8

import datetime
import numpy as np
import copy

from module import Module
from order import Order_module
from calendar import Calendar
from days import *
from employee import Employee
from equipment import Equipment
from module_type import Module_type
from mfg_step import Mfg_step
from step_type import Step_type
from factory import Factory

apsi3D = Factory('aPSI3D')


#CREATE EMPLOYEE
emp_1 = Employee(apsi3D, 12, 'James', "engineer", "technician")
emp_2 = Employee(apsi3D, 15, 'John', "technician")
emp_1.show()
emp_1.show_calendar()



# #CREATE EQUIPMENT
# equ_1 = Equipment(apsi3D, 'Equip_1', 'A', 12 )
# # equ_1.show()
# # equ_1.show_calendar()


# # CREATE STEP TYPES
# step_type_1 = Step_type(1, 'description_1', 'engineer', 'M1', 16, 8)
# step_type_2 = Step_type(2, 'description_2','technician', 'M2', 40, 4)


# # CREATE MODULE TYPE
# mod_1 = Module_type("Mod1")
# mod_1.add_step(step_type_1)
# mod_1.add_step(step_type_2, 1)
# # mod_1.show()


# #CREATE ORDER
# ord_1 = Order_module(apsi3D, mod_1, 2 )
# # ord_1.show()
# # ord_1.show_calendar()








