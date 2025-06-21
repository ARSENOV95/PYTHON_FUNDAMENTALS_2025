5population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

no_distribution = False

if not population:
    quit()

for index in range(len(population)): 
    welthiest = max(population)     #for each itteration we find the largest value in the list 
    if welthiest < minimum_wealth:  #if the max value is < then the min wealth then a distribution will not be possible and the loop is exited
        no_distribution = True
        break

    max_val_index = population.index(welthiest) #we find the index of the max value 

    if population[index] < minimum_wealth:
        add_wealth = (minimum_wealth - population[index])  #if the current value is < min wealth, then increase it with the amount needed to min waelth 
        
        if  population[max_val_index] - add_wealth >= minimum_wealth: #check the max value if we remove it form the list
            population[max_val_index] = population[max_val_index] - add_wealth #if yes we will deacrease it and add it the the elements 
            population[index] = population[index] + add_wealth
        else:
            no_distribution = True #else we will abort the loop meaning no other volue can be istributed as after each ittration we will re-assign the max value 
            break

if no_distribution:
    print("No equal distribution possible")
else:
    print(population)