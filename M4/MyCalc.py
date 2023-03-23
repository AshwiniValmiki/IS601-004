#Created a class named MyCalc

class MyCalc:

    #Defining the variable ans and initialising it to 0
    def __init__(self):
        self.ans = 0
    
    def add(self, x, y):
        self.ans = x+y
        return self.ans
    #Ucid : av659
    #Date : 02/22/23
    #Summary : Performing addition and storing the value in the variable ans and returning it 

    def subtract(self, x, y):
        self.ans = x-y
        return self.ans
    #Ucid : av659
    #Date : 02/22/23
    #Summary : Performing subtraction and storing the value in the variable ans and returning it 
    
    #Performing multiplication and storing the value in the variable ans and returning it 
    def multiply(self, x, y):
        self.ans = x*y
        return self.ans
    #Ucid : av659
    #Date : 02/22/23
    #Summary : Performing multiplication and storing the value in the variable ans and returning it 

    #Performing division and storing the value in the variable ans and returning it 
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Zero Division Error .Can't divide by zero. Kindly select a valid integer.")
            return self.ans        
        else:
            self.ans = x/y
            return self.ans
    #Ucid : av659
    #Date : 02/22/23
    #Summary : Performing division and storing the value in the variable ans and returning it    

#Defining a main function where we'll run the user input and call the above class to perform necessary operations
def main():
    calc = MyCalc()
    while True:
        #Asking for user input
        user_input = input("Enter any valid number, any valid math operator, and any valid number: ")
        try:
            tokens = user_input.split()
            if len(tokens) != 3:
                print("Invalid input. Please enter a valid expression.")
                continue
            #Asking for a first valid integer or variable ans which is the last answer stored
            num1 = float(tokens[0]) if tokens[0] != "ans" else calc.ans
            operator = tokens[1]
            #Asking for a second valid integer or variable ans which is the last answer stored
            num2 = float(tokens[2]) if tokens[2] != "ans" else calc.ans
            #Calling necessary operations by comapring user's opted operator 
            if operator == "+":
                result = calc.add(num1,num2)
            elif operator == "-":
                result = calc.subtract(num1,num2)
            elif operator == "*":
                result = calc.multiply(num1,num2)
            elif operator == "/":
                result = calc.divide(num1,num2)
            else:
                print("Invalid operator. Please enter a valid expression.")
                continue
            print(result)
        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
