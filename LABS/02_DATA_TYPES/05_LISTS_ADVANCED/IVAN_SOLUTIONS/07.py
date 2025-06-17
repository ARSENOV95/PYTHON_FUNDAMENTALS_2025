numbers = [int(num) for num in input().split(", ")]

group  = 10
while numbers:  #while len(numbers) > 0
    list_of_numbers =  [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    
    numbers = [number for number in numbers if not number in list_of_numbers]
    group += 10