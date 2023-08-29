#Author: Jordan Ehlinger
#Assignment Number & Name: HW8A Inheritance
#Due Date: N/A
#Program Description: Calculates information for production worker


#import classes from other files
import Ehlinger_Jordan_HW7_Validation_Class
import Ehlinger_Jordan_EmployeeFile

def main():
    #create variable for validation class and production worker class
    validation = Ehlinger_Jordan_HW7_Validation_Class.ValidationClass()
    production_employee_file = Ehlinger_Jordan_EmployeeFile.ProductionWorker()

    #get input for employee name and id and send them to employee class functions
    employee_name = input("Enter employee name: ")
    production_employee_file.set_employee_name(employee_name)
    employee_id = input("Enter employee ID: ")
    production_employee_file.set_employee_id(employee_id)

    #intentional bad value to initialize
    shift_number = -1
    #while loop to get shift number and run it through validation function
    while shift_number == -1:
        shift_number_input = input("Enter shift number: ")
        shift_number = validation.checkInteger(shift_number_input)
        if shift_number == -1:
            print("The shift number must be 1 or 2.")
    #send shift number to employee class functions
    production_employee_file.set_shift_number(shift_number)

    #intentional bad value to initialize
    pay_rate = -1
    #while loop to get pay rate and run it through validation function
    while pay_rate == -1:
        pay_rate_input = input("Enter pay rate: ")
        pay_rate = validation.checkFloat(pay_rate_input)
        if pay_rate == -1:
            print("The pay rate must be a positive number greater than 0.")
    #send pay rate to employee class functions
    production_employee_file.set_pay_rate(pay_rate)

    #intentional bad value to initialize
    hours_worked = -1
    #while loop to get hours worked and run it through validation function
    while hours_worked == -1:
        hours_worked_input = input("Enter hours worked: ")
        hours_worked = validation.checkFloat(hours_worked_input)
        if hours_worked == -1:
            print("Your hours worked must be a positive number greater than 0.")
    #send hours worked to employee class functions
    production_employee_file.set_hours_worked(hours_worked)

    #call function to calculate total pay
    production_employee_file.calculate_total_pay()

    print()
    print("Employee Name:", production_employee_file.get_employee_name())
    print("Employee ID:", production_employee_file.get_employee_id())
    print("Shift Number:", production_employee_file.get_shift_number())
    print("Pay Rate: $", format(pay_rate, '.2f'), "/hr", sep='')
    print("Hours Worked:", format(production_employee_file.get_hours_worked(), '.2f'))
    print("Total Pay: $", format(production_employee_file.get_pay_rate(), ',.2f'), sep='')


#call main
main()
