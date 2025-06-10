numbers = int(input())

available_commands = ("even","odd","psotive","negative")


list_of_numbers = []
result = []

for number in range(numbers):
    current_number = int(input())
    list_of_numbers.append(current_number)


    
command = input()

if command not in available_commands:
    quit()


for element in list_of_numbers:
    if command == "even":
        if element % 2 == 0:
            result.append(element)
    elif command == "odd":
        if element % 2 != 0:
            result.append(element)
    elif command == "positive":
        if element >= 0:
            result.append(element)
    elif command == "negative":
       if element < 0:
           result.append(element)


print(result)