def rate(additonal_info :str,plant_dict :dict)->dict:
    some_plant,some_rating = additonal_info.split(' - ')
    some_rating = int(some_rating)

    if some_plant in plant_dict.keys():
        if plant_dict[some_plant]['rating'] == 0.00:
            plant_dict[some_plant]['rating']  = some_rating
        else:
            plant_dict[some_plant]['rating']  =  (plant_dict[some_plant]['rating'] + some_rating)/2
    else:
        print("error")
    return plant_dict

def update(additonal_info :str,plant_dict :dict)->dict:
    some_plant,new_rarity = additonal_info.split(' - ')
    new_rarity = int(new_rarity)
    if some_plant in plant_dict.keys():
        plant_dict[some_plant]['rarity'] = new_rarity
    else:
        print("error")
    return plant_dict

def reset(additonal_info:str,plant_dict :dict)->dict:
    some_plant = additonal_info
    if some_plant in plant_dict.keys():
        plant_dict[some_plant]['rating'] = 0
    else:
        print("error")
    return plant_dict

##############################user input#################################
n = int(input())   
plants = {} 

for i in range(n):
    info = input().split('<->')
    plat,rarity = info[0],int(info[1])
    
    if plat not in plants.keys():
        plants[plat] = {'rarity':0,'rating': 0.00}
    plants[plat]['rarity'] = rarity

while (command := input()) != "Exhibition":
    parts = command.split(': ')
    action = parts[0]
    plant_rating = parts[1]

    match action:
        case "Rate":
            plants = rate(plant_rating,plants)          
        case "Update":
            plants = update(plant_rating,plants)   
        case "Reset":
            plants = reset(plant_rating,plants)

print("Plants for the exhibition:")

for curr_plant,info in plants.items():
    print(f"- {curr_plant}; Rarity: {info['rarity']}; Rating: {info['rating']:.2f}")
