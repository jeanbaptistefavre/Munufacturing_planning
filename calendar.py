#code:utf-8

import datetime
import numpy as np
from days import *



class Calendar():
    
    def __init__(self):
        self.calendar_tb = []

    
    def add_days_employee(self, day, month, year, start_hour, finish_hour, start_lunch, finish_lunch):
        self.calendar_tb.append((datetime.date(year, month, day), Days_employee(start_hour, finish_hour, start_lunch, finish_lunch)))


    def add_days_equipment(self, day, month, year, quantity):
        self.calendar_tb.append((datetime.date(year, month, day), Days_equipment(quantity)))


    def add_days_module(self, day, month, year):
        self.calendar_tb.append((datetime.date(year, month, day), Days_module()))


    def show(self):
        last_date = datetime.datetime.now() + datetime.timedelta(days=7)
        date = last_date.date()
        self.calendar_tb = sorted(self.calendar_tb, key=lambda tb: tb[0]) 
        for day in self.calendar_tb:
            if day[0] >= datetime.datetime.now().date() and day[0] <= date:
                print(f"Day {day[0]} :")
                day[1].show()



# class Calendar():
    
#     def __init__(self):
#         self.calendar_dic = {}

    
#     def add_days_employee(self, day, month, year, start_hour, finish_hour, start_lunch, finish_lunch):
#         self.calendar_dic[datetime.date(year, month, day)] = Days_employee(start_hour, finish_hour, start_lunch, finish_lunch)


#     def add_days_equipment(self, day, month, year, quantity):
#         self.calendar_dic[datetime.date(year, month, day)] = Days_equipment(quantity)


#     def add_days_module(self, day, month, year):
#         self.calendar_dic[datetime.date(year, month, day)] = Days_module()


#     def show(self):
#         last_date = datetime.datetime.now() + datetime.timedelta(days=7)
#         date = last_date.date()
#         for key, day in self.calendar_dic.items():
#             if key >= datetime.datetime.now().date() and key <= date:
#                 print(f"Day {key} :")
#                 day.show()