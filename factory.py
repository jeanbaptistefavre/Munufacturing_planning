#code:utf-8

import datetime
import numpy as np
from calendar import Calendar
from days import *

class Factory():


    def __init__(self, name):
        self.name = name
        self.list_employees = []
        self.list_equipment = []
        self.list_orders = []

    
    def show_employees(self):
        print('List of employees :')
        for employee in self.list_employees:
            employee.show()
    
    
    def show_orders(self):
        print('List of orders :')
        for order in self.list_orders:
            order.show()


    def show_equipment(self):
        print('List of equipment :')
        for equipment in self.list_equipment:
            equipment.show()