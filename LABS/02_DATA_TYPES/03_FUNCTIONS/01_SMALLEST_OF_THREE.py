
def smallest_of_three():
    list_of_numbers = []
    
    for number in range(3):
        current_number = int(input())
        
        list_of_numbers.append(current_number)
    
    return min(list_of_numbers)

print(smallest_of_three())