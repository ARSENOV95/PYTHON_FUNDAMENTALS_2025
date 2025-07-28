#function to rate a plant if present in the dicitoanry
def rate(additonal_info :str,plant_dict :dict)->dict:
    some_plant,some_rating = additonal_info.split(' - ')
    some_rating = int(some_rating)

    if some_plant in plant_dict.keys():
        if plant_dict[some_plant]['rating'] == 0.00:
            plant_dict[some_plant]['rating']  = some_rating
        else:
            plant_dict[some_plant]['rating']  =  (plant_dict[some_plant]['rating'] + some_rating)/2 
            #if a a ratings is pesent we add the new one ot the old and devide by 2 to take the average
    else:
        print("error")
    return plant_dict

#function to update the rarity of a plant if present in the dicitoanry (if the plany is present)
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
plants = {}   #dictionary to store the results 

for i in range(n):  # a loop to fill the list
    info = input().split('<->')
    plat,rarity = info[0],int(info[1])
    
    if plat not in plants.keys():                
        plants[plat] = {'rarity':0,'rating': 0.00}  #if the plant is not i nthe citionary, set dummy values for rarity and the ratings which we will add
    plants[plat]['rarity'] = rarity #add the rarity

while (command := input()) != "Exhibition": #if while the commands is != trigger to storp the loop split it ot several parts 
    parts = command.split(': ')
    action = parts[0]
    plant_rating = parts[1]

    #perform actions on the dictonary depending on the command
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
