num_lines = int(input())

for line in range(num_lines):
    current_line = input()
    
    #find the name in the string
    fist_boundery_name = current_line.find('@') + 1
    last_boundery_name = current_line.find('|')

    name = current_line[fist_boundery_name:last_boundery_name]

    #find the age in the string
    fist_boundery_age = current_line.find('#') + 1
    last_boundery_name = current_line.find('*')

    age = current_line[fist_boundery_age:last_boundery_name]

    print(f"{name} is {age} years old.")