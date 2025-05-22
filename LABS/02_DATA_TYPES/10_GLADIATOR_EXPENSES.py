number_of_lost_fights = int(input())

#all prices are directly input in a dicitoanry
repair_price = {
'helmet': float(input()),
'sword': float(input()),               
'shield': float(input()),
'armour': float(input())
}

total_repair_expenses = 0  #vairable to hold the totla repair bill
#shield_repair = 0  >>>>>   used for v2 

for fight_number in range(1,number_of_lost_fights + 1):
    
    #if 2,4,6 ... add the prices for a helment
    if fight_number %2 == 0:
        total_repair_expenses += repair_price['helmet']
    
    if fight_number %3 == 0: #if 3,6,9... add price for the sword
         total_repair_expenses += repair_price['sword']  
         if fight_number %2 == 0:  #if 6,12,18.. add price for the sheild 
             total_repair_expenses += repair_price['shield'] 
             #shield_repair += 1   >>>>>   used for v2 
             
    if fight_number %12 == 0:  #if 12,24 ... the shield would ahve broken twice and we add the price of the armour 
       total_repair_expenses += repair_price['armour']  

    #==============v2=========================================
    #if shield_repair == 2:
    #    total_repair_expenses += repair_price['armour']  
    #    shield_repair = 0

print(f"Gladiator expenses: {total_repair_expenses:.2f} aureus")


