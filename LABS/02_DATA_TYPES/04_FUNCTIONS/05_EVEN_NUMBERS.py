list_of_strings = input().split(" ") #takes a stirng and splits it into a list with " " as a separator

list_of_numbers = [int(num) for num in list_of_strings] #we convert each element of tje strng to a number 

def is_even(number : int):  #function to check if a number is even (truns True or False)
    return number %2 == 0

result = list(filter(is_even,list_of_numbers)) #a lsit to store olny the even numebrs
#filter - a function which takes another functions for an argument and a list or other iterable 
# it checks the value 1 by 1 so the variable wich we use to store the result should be a list or tuple

print(result) 