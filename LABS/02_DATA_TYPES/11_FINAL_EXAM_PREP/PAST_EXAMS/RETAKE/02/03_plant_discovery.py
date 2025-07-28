
def rate (some_list :str,some_plants :dict,some_plant_rating:dict)->dict:
    parts = some_list.split(' - ')
    plant,rating = parts[0],int(parts[1])

    if plant not in some_plant_rating.keys():
        some_plant_rating[plant] = {'rarity':some_plants[plant],'rating':rating}
    elif plant in some_plant_rating.keys():
        if some_plant_rating[plant]['rating'] == 0:
            some_plant_rating[plant]['rating'] = rating
        else:
             some_plant_rating[plant]['rating'] = (some_plant_rating[plant]['rating'] + rating)/2
    return some_plant_rating


n = int(input())

plants = {}
plants_ratings = {}

for i in range(n):
    info = input().split('<->')
    plat,rarity = info[0],int(info[1])
    
    if plat not in plants.keys():
        plants[plat] = 0
    plants[plat] = rarity

while (command := input()) != 'Exhibition':
    parts = command.split(':')
    action = parts[0]
    plant_rating = parts[1]

    match action:
        case 'Rate':
            plants_ratings = rate(plant_rating,plants,plants_ratings)
        case 'Update':
            pass
        case 'Reset':
            pass

print(plants_ratings)