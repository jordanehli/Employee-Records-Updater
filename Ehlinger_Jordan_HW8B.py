#Author: Jordan Ehlinger
#Assignment Number & Name: HW8B Inheritance
#Due Date: N/A
#Program Description: Calculates information for shift supervisor


#import classes from other files
import Ehlinger_Jordan_HW7_Validation_Class
import Ehlinger_Jordan_EmployeeFile

def main():
    #create variable for validation class and shift supervisor class
    validation = Ehlinger_Jordan_HW7_Validation_Class.ValidationClass()
    supervisor_employee_file = Ehlinger_Jordan_EmployeeFile.ShiftSupervisor()

    #get input for employee name and id and send them to employee class functions
    employee_name = input("Enter employee name: ")
    supervisor_employee_file.set_employee_name(employee_name)
    employee_id = input("Enter employee ID: ")
    supervisor_employee_file.set_employee_id(employee_id)

    #intentional bad value to initialize
    salary = -1
    #while loop to get salary and run it through validation function
    while salary == -1:
        salary_input = input("Enter salary: ")
        salary = validation.checkFloat(salary_input)
        if salary == -1:
            print("The salary must be a positive number greater than 0.")
    #send salary to supervisor class functions
    supervisor_employee_file.set_salary(salary)

    #intentional bad value to initialize
    production_bonus = -1
    #while loop to get bonus and run it through validation function
    while production_bonus == -1:
        production_bonus_input = input("Enter production bonus: ")
        production_bonus = validation.checkFloat(production_bonus_input)
        if production_bonus == -1:
            print("The production bonus must be a positive number greater than 0.")
    #send bonus to supervisor class functions
    supervisor_employee_file.set_production_bonus(production_bonus)

    #call function to calculate total pay
    supervisor_employee_file.calculate_total_pay()

    #call string function to display outputs
    print(supervisor_employee_file)


#call main
main()

