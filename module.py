#code:utf-8

import datetime
import numpy as np
import copy
from functions import *
from calendar import Calendar
from days import *
from module_type import Module_type
from settings import *



class Module():
    
    def __init__(self, order_module, number):
        self.module_id = str(order_module.order_id) + '-' + str(number)
        self.order_module = order_module
        self.calendar = Calendar()
        self.last_step_completed = ''
        self.steps_left = copy.deepcopy(self.order_module.module_type.steps)
        self.pointer = (datetime.datetime.now().date(), 0)  #(date, intervalle)
        self.state = 'ready for the next step'

        self.create_calendar()
        self.Place_in_calendar()

    
    def create_calendar(self):
        for n in range(100):
            new_date = datetime.datetime.today() + datetime.timedelta(days=n)
            day = new_date.day
            month = new_date.month
            year = new_date.year
            self.calendar.add_days_module(day, month, year)


    def Place_in_calendar(self):
        #FINDING A SLOT FOR THE MODULE
        while len(self.steps_left) > 0:
            step = self.steps_left.pop(0)                                       #Next manufacturing step
            step_nb_inter = step.step_type.duration_intervalle                  #Duration (in time slots)
            step_skill = a.step_type.employee_skill                             #Skills required
            step_equipment = a.step_type.equipment_type                         #Equipment required
            # print(step_nb_inter, step_skill, step_equipment)
            module_slot_found = False                                            #True when the manufacturing step is placed in employee and machine calendar

            while not module_slot_found:
                #EMPLOYEE SLOT
                employee_sel = self.place_in_calendar_employee(step, step_nb_inter, step_skill)   
                self.pointer = employee_sel[1]
                #EQUIPMENT SLOT
                equipment_sel = self.place_in_calendar_equipment(step, step_nb_inter, step_equipment)                                          

                if pointer_employee[1] == pointer_equipment[1] 
                or pointer_employee[2] == pointer_equipment[2]:
                    module_slot_found == True
                    self.modify_module_calendar(step, step_nb_inter)
                    self.modify_employee_calendar(step, step_nb_inter, employee_sel[1])
                    self.modify_equipment_calendar(step, step_nb_inter, equipment_sel[1])
                    self.pointer[1] += step_nb_inter


    def modify_module_calendar(self, step, step_nb_inter):            
        for date in self.calendar_tb:                                                       
            if date[0] = self.pointer[0]:                                                   
                day = date[1]                                                            
                for slot in range(self.pointer[1], self.pointer[1] + step_nb_inter):    
                    day[slot] = step.step_type.step_id



#FUNCTIONS LINKED TO EMPLOYEE

    def check_slot_employee(self, slots, step, step_nb_inter, day, employee_pointer):
    #Checks if an employee has a slot of the time of the step that fulfills all the requirements
        employee_slot = 0                                       #counter: if 5 is reached, the employee slot is found
        for n in range(0, step_nb_inter):                       #for each slot of the group of slots    
            if day[slots + n][0] == 1:                          #If employee is at work
                if day[slots + n][1] == 'null' or               #If the employee is not working on a task
                day[slots + n][1] == step.step_type.step_id:    #or if he is working on the same step for another module
                    if day[slots + n][2] == 1:                  #if it the work on the step has not star    previous timeslot
                        employee_slot += 1                      # +1 if slot works
                    else:                                       
                        break                                   #condition not fulfilled, try next group of slots
                else:
                    break                                       #condition not fulfilled, try next group of slots
            else:
                break                                           #condition not fulfilled, try next group of slots
        if employee_slot == 5:                  
            return True, slots
        else:
            return False, 0


    def place_in_calendar_employee(self, step, step_nb_inter, step_skill):
    #Find a time slot for an employee
        latest_date = datetime.datetime.now() + datetime.timedelta(days=300)        #The slot must be found in the next 300 days
        employee_pointer = (latest_date.date(), 0)
        employee_selected = []
        for employee in self.order_module.factory.list_employees:                   #For each employee in the factory
            if step_skill in employee.skills:                                       #If the employee has the skill required
                slot_employee_found == False                                        #True when a suggestion for the slot will be found
                for date in employee.calendar_tb:                                   #for each day of the calendar (date, day[])
                    if date[0] = self.pointer[0]:                                   #if the date is equal to the date of the pointer
                        day = date[1]                                               #the day[] is the second element of the tuple
                        for slots in range(NB_TIME_SLOT - step_nb_inter):           #try every continuous group of slots in a day
                            if slots >= self.pointer[1]:                            #if the slot is after the pointer
                                slot_employee_found, slot_pointer = self.check_slot_employee(slots, step, step_nb_inter, day, employee_pointer) #true if slot found
                                if slot_employee_found == True:
                                    break                                                   #if slot found, exit the loops
                        if slot_employee_found == True:
                            employee_pointer_2 = (date, slot_pointer)
                            break
                    elif date[0] > self.pointer[0] and date[0] <= employee_pointer[0]:       #if the date after date of the module pointer and before the employee points
                        day = date[1]                                                       #the day[] is the second element of the tuple
                        for slots in range(NB_TIME_SLOT - step_nb_inter):                   #try every continuous group of slots in a day
                            slot_employee_found, slot_pointer = self.check_slot_employee(slots, step, step_nb_inter, day, employee_pointer)
                            if slot_employee_found == True:
                                break               
                        if slot_employee_found == True:
                            employee_pointer_2 = (date, slot_pointer)
                            break
                if pointer_1_smaller(employee_pointer_2, employee_pointer):
                    employee_selected = [employee, employee_pointer_2]
                    employee_pointer = employee_pointer_2
        return employee_selected


    def modify_employee_calendar(self, step, step_nb_inter, pointer_employee):            
        for date in pointer_employee[0].calendar_tb:                                                       
            if date[0] = pointer_employee[1][0]:                                                   
                day = date[1]                                                            
                for slot in range(pointer_employee[1][1] + 1, pointer_employee[1][1] + step_nb_inter):    
                    day[slot][1] = step.step_type.step_id
                    day[slot][2] = 0
                day[pointer_employee[1][1]][1] = step.step_type.step_id
                day[pointer_employee[1][1]][2] = 0


#FUNCTIONS LINKED TO EQUIPMENT

    def check_slot_equipment(self, slots, step, step_nb_inter, day, equipment_pointer):
    #Checks if an equipment has a slot of the time of the step that fulfills all the requirements
        equipment_slot = 0                                       #counter: if 5 is reached, the equipment slot is found
        for n in range(0, step_nb_inter):                       #for each slot of the group of slots    
            if day[slots + n][0] >= 1:                          #If the equipment has one at least room for one more module
                if day[slots + n][1] == 'null' or               #If the equipment is available
                day[slots + n][1] == step.step_type.step_id:    #or if he is working on the same step for another module
                    equipment_slot += 1
                else:
                    break                                       #condition not fulfilled, try next group of slots
            else:
                break                                           #condition not fulfilled, try next group of slots
        if equipment_slot == 5:                  
            return True, slots
        else:
            return False, 0


    def place_in_calendar_equipment(self, step, step_nb_inter, step_equipment):
    #Find a time slot for an equipment
        latest_date = datetime.datetime.now() + datetime.timedelta(days=300)        #The slot must be found in the next 300 days
        equipment_pointer = (latest_date.date(), 0)
        equipment_selected = []
        for equipment in self.order_module.factory.list_equipment:                  #For each equipment in the factory
            if step_equipment in equipment.equip_type:                              #If the equipment is of the right type
                slot_equipment_found == False                                       #True when a suggestion for the slot will be found
                for date in equipment.calendar_tb:                                  #for each day of the calendar (date, day[])
                    if date[0] = self.pointer[0]:                                   #if the date is equal to the date of the pointer
                        day = date[1]                                               #the day[] is the second element of the tuple
                        for slots in range(NB_TIME_SLOT - step_nb_inter):           #try every continuous group of slots in a day
                            if slots >= self.pointer[1]:                            #if the slot is after the pointer
                                slot_equipment_found, slot_pointer = self.check_slot_equipment(slots, step, step_nb_inter, day, equipment_pointer) #true if slot found
                                if slot_equipment_found == True:
                                    break                                                   #if slot found, exit the loops
                        if slot_equipment_found == True:
                            equipment_pointer_2 = (date, slot_pointer)
                            break
                    elif date[0] > self.pointer[0] and date[0] <= equipment_pointer[0]:       #if the date after date of the module pointer and before the equipment points
                        day = date[1]                                                       #the day[] is the second element of the tuple
                        for slots in range(NB_TIME_SLOT - step_nb_inter):                   #try every continuous group of slots in a day
                            slot_equipment_found, slot_pointer = self.check_slot_equipment(slots, step, step_nb_inter, day, equipment_pointer)
                            if slot_equipment_found == True:
                                break               
                        if slot_equipment_found == True:
                            equipment_pointer_2 = (date, slot_pointer)
                            break
                if pointer_1_smaller(equipment_pointer_2, equipment_pointer):
                    equipment_selected = [equipment, equipment_pointer_2]
                    equipment_pointer = equipment_pointer_2
        return equipment_selected



    def modify_equipment_calendar(self, step, step_nb_inter, pointer_equipment):            
        for date in pointer_equipment[0].calendar_tb:                                                       
            if date[0] = pointer_equipment[1][0]:                                                   
                day = date[1]                                                            
                for slot in range(pointer_equipment[1][1] + 1, pointer_equipment[1][1] + step_nb_inter):    
                    day[slot][0] -= 1
                    day[slot][1] = step.step_type.step_id
                    day[slot][2] = 0
                day[pointer_equipment[1][1]][0] -= 1
                day[pointer_equipment[1][1]][1] = step.step_type.step_id
                day[pointer_equipment[1][1]][2] = 0


    #SHOW FUNCTIONS

    def show_state(self):
        print(f"The module {self.module_id} is {self.state}.")
        if self.last_step_completed != '':
            print(f"The last step completed was {self.last_step_completed}")


    def show_calendar(self):
        print(f"The calendar of the module {self.module_id} is :")
        self.calendar.show()


