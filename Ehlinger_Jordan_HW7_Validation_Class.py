#Author: Jordan Ehlinger
#Assignment Number & Name: HW7 Return on Investment - Validation Class (Edited for HW8)
#Due Date: N/A
#Program Description: Validation class that holds one method to validate float and one method to validate integers


#create validation class
class ValidationClass:
    #input validation function for checking a float
    def checkFloat(self, input_value):
        try:
            float_value = float(input_value)
        except:
            return -1

        #check if input is positive
        if float_value <= 0:
            return -1
        else:
            return float_value
            
    #input validation function for checking an integer
    def checkInteger(self, input_value):
        try:
            integer_value = int(input_value)
        except:
            return -1

        #check if input is positive
        if integer_value != 1 and integer_value !=2:
            return -1
        else:
            return integer_value
