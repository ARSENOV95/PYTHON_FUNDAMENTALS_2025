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
        for arg in args:
            if arg not in initial_loot:
                initial_loot.insert(0,arg)

    elif text == "Drop":
        index = int(args[0])
        if not valid_index(index,initial_loot):
            continue

        removed_item = initial_loot.pop(index)

        initial_loot.append(removed_item)

    elif text == "Steal":

        steal_count = int(args[0]) #number of items to steal example 3

        if steal_count > len(initial_loot):  #if number of items is igbber then the list
            steal_count = len(initial_loot)

        #we are going to mae a renge which weill be the range of items stolef rome the list

        stolen_items = initial_loot[-steal_count:] #counts ofrm the enf of the list backowrds meaning 3 elements fro mthe last one - 7,6,5
        del initial_loot[-steal_count:]

for itm in initial_loot:
        len_of_all_loot += len(itm)


if len(initial_loot) > 0:
    average = len_of_all_loot / len(initial_loot)
    if stolen_items:
        print(", ".join(stolen_items))
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    if stolen_items:
        print(", ".join(stolen_items))
    print("Failed treasure hunt.")







