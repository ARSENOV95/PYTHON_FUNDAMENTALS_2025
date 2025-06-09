def calculate_facturial(some_number :int):
    for current_number in range(1,some_number):
        some_number *= current_number
    
    return some_number





first_number = int(input())
second_number = int(input())
first_facturial = calculate_facturial(first_number)
second_facturial = calculate_facturial(second_number)
print(f"{first_facturial/second_facturial:.2f}")
