materails = {"shards":0,
             "fragments":0,
             "motes":0}

got_legendary_item = False

while not got_legendary_item:
    current_item = input().split()
    for index in range(0,len(current_item),2):
        value = int(current_item[index])
        key = current_item[index+1].lower()

        if key not in materails:
           materails[key] = 0
        materails[key] += value

        if materails["shards"] >= 250:
            materails["shards"]  -= 250
            print("Shadowmourne obtained!")
            got_legendary_item = True
        elif materails["fragments"] >= 250:
            materails["fragments"]  -= 250
            print("Valanyr obtained!")
            got_legendary_item = True
        elif materails["motes"] >= 250:
            materails["motes"]  -= 250
            print("Dragonwrath obtained!")
            got_legendary_item = True

        if  got_legendary_item:
            break

for material,quantity in materails.items():
    print(f"{material}: {quantity}")

         