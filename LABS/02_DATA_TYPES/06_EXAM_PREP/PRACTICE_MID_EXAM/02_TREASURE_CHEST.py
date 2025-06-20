def valid_index(idx: int, seq: list) -> bool:
    return idx in range(len(seq))

initial_loot = input().split("|")
stolen_items = []
len_of_all_loot = 0

while True:
    command = input()

    if command == "Yohoho!":
        break

    text, *args = command.split()

    if text == "Loot" and len(args) > 0:
        [initial_loot.insert(0, arg) for arg in args if arg not in initial_loot]
        # insert the item if not == to any itrem of the list

    elif text == "Drop":
        args[0] = int(args[0])
        if not valid_index(args[0],initial_loot):
            continue

        removed_item = initial_loot.pop(args[0])
        initial_loot.append(removed_item)

    elif text == "Steal":

        steal_count = int(args[0]) #number of items to steal example 3

        if steal_count < 0:
            continue


        if steal_count > len(initial_loot):  #if number of items is igbber then the list 
            steal_count = len(initial_loot)

        #we are going to mae a renge which weill be the range of items stolef rome the list 

        end_interval = len(initial_loot)
        start_interval = end_interval - steal_count

        stolen_items = initial_loot[-steal_count:]
        print(stolen_items)

        #stolen_items = initial_loot[start_interval:end_interval]

        #for item in stolen_items:
        #    if item in initial_loot:
        #        initial_loot.remove(item)

for itm in initial_loot:
        len_of_all_loot += len(itm)


if initial_loot:
    average = len_of_all_loot / len(initial_loot)
    print(", ".join(stolen_items))
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print(", ".join(stolen_items))
    print("Failed treasure hunt.")







