number_of_electrons = int(input())

shells = []

number_of_shell = 0

while number_of_electrons > 0:

    number_of_shell += 1 
    max_electrons_in_shell = 2*(number_of_shell**2)

    if number_of_electrons >= max_electrons_in_shell:
        shells.append(max_electrons_in_shell)
    else:
        shells.append(number_of_electrons)
         
    number_of_electrons -= max_electrons_in_shell

print(shells)