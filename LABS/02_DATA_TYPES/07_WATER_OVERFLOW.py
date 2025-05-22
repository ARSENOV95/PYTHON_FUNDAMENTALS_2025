
number_of_pours = int(input())


tank_capacity  = 250 #LITERS #variable to hlod the total tank capacity
liters_poured = 0 #variable to store the amount of leters poured 

for current_pour in range(number_of_pours): # a loop to inititate a pour of water for the total number of pours 
    amount_of_water = int(input()) #amount of water to be poured on pass

    if tank_capacity - amount_of_water < 0: #if the capacitiy after current pour will be negative print message  and continue
        print("Insufficient capacity! ")
        continue
    else:
        liters_poured += amount_of_water #else substract the liters for mthe capacity and add them to the counter for poured water
        tank_capacity -= amount_of_water
        

print(liters_poured)


