def smallest_number(first_number :int,second_number :int,third_number : int):
    list_with_numbers = [first_number,second_number,third_number]
    return min(list_with_numbers)

first_number = int(input())  
second_number = int(input())  
third_number = int(input())  

print(smallest_number(first_number,second_number,third_number))
