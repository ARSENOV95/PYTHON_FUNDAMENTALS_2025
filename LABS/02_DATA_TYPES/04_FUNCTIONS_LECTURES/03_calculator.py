def addition(a :int,b :int):
    return a + b

def subtraction(a :int,b :int):
    return a - b
    

def multiplication(a :int,b :int):
    return a * b 

def devision(a :int,b :int):
    return a / b

def calculator():
    operation = input()
    number_1 = int(input())
    number_2 = int(input())

    if operation == "multiply":
        result  = multiplication(a=number_1,b=number_2)
        
    
    elif operation == "divide":
        result  = devision(a=number_1,b=number_2)
        

    elif operation == "add":
        result  = addition(a=number_1,b=number_2)
        
    
    elif operation == "subtract":
        result  = subtraction(a=number_1,b=number_2)
        
    
    print(result)



calculator()