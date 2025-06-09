def even(n :int) -> bool: 
    return  n %2 == 0

numbers_as_string  = input().split()
numbers_as_digits  = []


for number in numbers_as_string:
    numbers_as_digits.append(int(number))

final_result = list(filter(even,numbers_as_digits))
print(final_result)