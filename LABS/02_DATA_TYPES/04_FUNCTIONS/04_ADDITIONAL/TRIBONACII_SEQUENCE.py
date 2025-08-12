def tribunacii_sequence(num :int)->str:
    list_of_numbers = []
    
    for i in range(num):
        number = sum(list_of_numbers[-3:])
        list_of_numbers.append(number)
    return print(' '.join([str(char) for char in list_of_numbers]))

number_of_digits = int(input())

tribunacii_sequence(number_of_digits)