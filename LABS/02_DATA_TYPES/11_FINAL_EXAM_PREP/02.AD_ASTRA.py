import re

food_supply = input()

daily_calories = 2000
total_calories = 0

food_info = {}


pattern = r'(?i)#([a-z\s]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#|\|([a-z\s]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\|'

match = re.finditer(pattern,food_supply)

if match:
    for supply in match:
        #filter to clear out then none values for meach iter
        supplies = list(filter(lambda x: x!= None,supply.groups()))
        total_calories += int(supplies[2])
        food_info[supplies[0]] = [supplies[1],supplies[2]]

print(f"You have food to last you for: {total_calories//daily_calories} days!")

for food,info in food_info.items():
    print(f"Item: {food}, Best before: {info[0]}, Nutrition: {info[1]}")