#code:utf-8

import datetime
import numpy as np
from module import Module
from calendar import Calendar
from factory import Factory

class Order_module():
    
    order_count = 1

    def __init__(self, factory, module_type, quantity):
        self.order_id = Order_module.order_count
        self.module_type = module_type
        self.quantity = quantity
        self.modules = []
        self.factory = factory
        self.add_order()
        self.create_modules()
        
        Order_module.order_count += 1
    
    def create_modules(self):
        for i in range(1, int(self.quantity) + 1):
            module = Module(self, i)
            self.modules.append(module)


    def show_modules(self):
        print(f"The modules in the order '{self.order_id}'  are at the following states:")
        for module in self.modules:
            module.show_state()

    
    def show_calendar(self):
        print(f"The calendars of the modules in the order '{self.order_id}'  are as followed:")
        for module in self.modules:
            module.show_calendar()


    def show(self):
        print(f"{self.order_id} : {self.quantity} of {self.module_type}.")
        for module in self.modules:
            module.show_calendar()


    def add_order(self):
        self.factory.list_orders.append(self)