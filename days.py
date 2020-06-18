#code:utf-8

import datetime
import numpy as np
from settings import *


class Days_employee():

    def __init__(self, start_hour=0, finish_hour=24, start_lunch=0, finish_lunch=0):
        self.nb_intervalles = NB_TIME_SLOT
        self.day_tb = []
        self.start_intervalle = int((start_hour * 60) // INTERVALLE)
        self.finish_intervalle =int((finish_hour * 60) // INTERVALLE)
        self.start_lunch_intervalle = int((start_lunch * 60) // INTERVALLE)
        self.finish_lunch_intervalle = int((finish_lunch * 60) // INTERVALLE)

        self.fill_in_tb()
        

    def fill_in_tb(self):
        for i in range(self.start_intervalle):
            self.day_tb.append((0, 'null', 1))
        for i in range(self.start_lunch_intervalle - self.start_intervalle):
            self.day_tb.append((1, 'null', 1))
        for i in range(self.finish_lunch_intervalle - self.start_lunch_intervalle):
            self.day_tb.append((0, 'null', 1))
        for i in range(self.finish_intervalle - self.finish_lunch_intervalle):
            self.day_tb.append((1, 'null', 1))
        for i in range(self.nb_intervalles - self.finish_intervalle):
            self.day_tb.append((0, 'null', 1))


    def show(self):
        print(self.day_tb)



class Days_equipment():

    def __init__(self, max_quantity):
        self.nb_intervalles = int((24 * 60) // INTERVALLE)
        self.day_tb = []
        self.quantity_available = max_quantity

        self.fill_in_tb()
        

    def fill_in_tb(self):
        for i in range(self.nb_intervalles):
            self.day_tb.append((self.quantity_available, 'null', 1))


    def show(self):
        print(self.day_tb)



class Days_module():

    def __init__(self):
        self.nb_intervalles = int((24 * 60) // INTERVALLE)
        self.day_tb = []

        self.fill_in_tb()
        

    def fill_in_tb(self):
        for i in range(self.nb_intervalles):
            self.day_tb.append('null')
            

    def show(self):
        print(self.day_tb)