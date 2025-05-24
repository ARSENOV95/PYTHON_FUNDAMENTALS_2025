number_of_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

total_helmets_broken =  number_of_fights // 2
total_sword_broken =  number_of_fights // 3
total_shiled_broken =  number_of_fights // (2*3)
total_armour_broken =  total_shiled_broken // 2

expenses = ((total_helmets_broken * helmet_price) + \
            (total_sword_broken * sword_price) + \
            (total_shiled_broken * shield_price)+ \
            (total_armour_broken * armour_price))

print(f"Gladiator expenses: {expenses} aureus")
