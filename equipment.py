#code:utf-8

import datetime
import numpy as np
from calendar import Calendar
from days import *
from factory import Factory


class Equipment():
    
    def __init__(self, factory, equip_id, equip_type, max_quantity):
        self.factory = factory
        self.equip_id = equip_id 
        self.equip_type = equip_type
        self.max_quantity = max_quantity
        self.calendar = Calendar()

        self.create_calendar()

    def show(self):
        print(f"Equipment ID : {self.equip_id}; Type : {self.equip_type}; Maximum quantity : {self.max_quantity}")

    
    def create_calendar(self):
        for n in range(1000):
            new_date = datetime.datetime.today() + datetime.timedelta(days=n)
            day = new_date.day
            month = new_date.month
            year = new_date.year
            self.calendar.add_days_equipment(day, month, year, self.max_quantity)
    

    def show_calendar(self):
        print(f"The calendar of the Equipment {self.equip_id} is:")
        self.calendar.show()


    def add_equipment(self):
        self.factory.list_equipment.append(self)