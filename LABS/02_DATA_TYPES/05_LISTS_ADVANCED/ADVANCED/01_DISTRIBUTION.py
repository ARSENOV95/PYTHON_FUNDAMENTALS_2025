population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

no_distribution = False

for index in range(len(population)):
    welthiest = max(population)
    if welthiest < minimum_wealth:
        no_distribution = True
        break

    max_val_index = population.index(welthiest)

    if population[index] < minimum_wealth:
        add_wealth = minimum_wealth - population[index]
        
        if  population[max_val_index] - add_wealth >= minimum_wealth:
            population[max_val_index] = population[max_val_index] - add_wealth
            population[index] = population[index] + add_wealth
        else:
            no_distribution = True
            break

if no_distribution:
    print("No equal distribution possible")
else:
    print(population)