first_number = int(input())
second_number = int(input())

def factorial_division(num1 = 1 ,  num2  = 1 ):
    from math import factorial #from the math module we only import the fuction to calculate the factorial

    fact_first = factorial(num1)
    fact_second = factorial(num2)

    result = f"{fact_first/fact_second:.2f}"


    return result

print(factorial_division(first_number,second_number))