#code:utf-8

import datetime
import numpy as np
from calendar import Calendar
from days import *
from factory import Factory

class Employee():


    
    def __init__(self, factory, employee_id, name, *skill):
        self.factory = factory
        self.employee_id = employee_id
        self.name = name
        self.skills = skill
        self.calendar = Calendar()
        self.start_hour = 8
        self.finish_hour = 18
        self.start_lunch = 12
        self.finish_lunch = 13.5

        self.create_calendar()
        self.add_employee()


    def show(self):
        print(f"Employee ID : {self.employee_id}; Name : {self.name}; Skills : {self.skills}.")


    def create_calendar(self):
        for n in range(1000):
            new_date = datetime.datetime.today() + datetime.timedelta(days=n)
            if new_date.weekday() != 5 and new_date.weekday() != 6:
                day = new_date.day
                month = new_date.month
                year = new_date.year
                self.calendar.add_days_employee(day, month, year, self.start_hour, self.finish_hour, self.start_lunch, self.finish_lunch)


    def show_calendar(self):
        print(f"The calendar of the employee with the ID {self.employee_id} is:")
        self.calendar.show()


    def add_skill(self, skill):
        self.skills.append(skill)
    

    def add_employee(self):
        self.factory.list_employees.append(self)