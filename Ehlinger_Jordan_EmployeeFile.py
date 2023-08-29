#Author: Jordan Ehlinger
#Assignment Number & Name: HW8 Inheritance - Employee File
#Due Date: N/A
#Program Description: Holds class for employee, production worker, and shift supervisor

#Employee superclass
class Employee:
    #init function for employee name and id
    def __init__(self):
        self.__employee_name = ""
        self.__employee_id = ""

    #set functions for employee name and id
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    #get functions for employee name and id
    def get_employee_name(self):
        return self.__employee_name
    def get_employee_id(self):
        return self.__employee_id


#ProductionWorker subclass
class ProductionWorker(Employee):
    #init function for superclass attributes and subclass attributes
    def __init__(self):
        #call superclass attributes
        Employee.__init__(self)
        #initialize new attributes
        self.__shift_number = 0
        self.__pay_rate = 0
        self.__hours_worked = 0

    #set functions for shift number, pay rate, and hours worked
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    #get functions for shift number, pay rate, and hours worked
    def get_shift_number(self):
        return self.__shift_number
    def get_pay_rate(self):
        return self.__pay_rate
    def get_hours_worked(self):
        return self.__hours_worked

    #function to calculate total pay
    def calculate_total_pay(self):
        self.__pay_rate = self.__pay_rate * self.__hours_worked


#ShiftSupervisor subclass
class ShiftSupervisor(Employee):
    #init function for superclass attributes and subclass attributes
    def __init__(self):
        #call superclass attributes
        Employee.__init__(self)
        #initialize new attributes
        self.__salary = 0
        self.__production_bonus = 0
        self.__total_pay = 0

    #set functions for salary and production bonus
    def set_salary(self, salary):
        self.__salary = salary
    def set_production_bonus(self, production_bonus):
        self.__production_bonus = production_bonus

    #get functions for salary, production bonus, and total pay
    def get_salary(self):
        return self.__salary
    def get_production_bonus(self):
        return self.__production_bonus
    def get_total_pay(self):
        return self.__total_pay

    #function for calculating total pay
    def calculate_total_pay(self):
        self.__total_pay = self.__salary + self.__production_bonus

    #string function to display outputs
    def __str__(self):
        supervisor_output = "\nEmployee Name: " + self.get_employee_name() + "\n"
        supervisor_output += "Employee ID: " + self.get_employee_id() + "\n"
        supervisor_output += "Salary: $" + format(self.get_salary(), ',.2f') + "\n"
        supervisor_output += "Production Bonus: $" + format(self.get_production_bonus(), ',.2f') + "\n"
        supervisor_output += "Total Pay: $" + format(self.get_total_pay(), ',.2f')
        return supervisor_output



