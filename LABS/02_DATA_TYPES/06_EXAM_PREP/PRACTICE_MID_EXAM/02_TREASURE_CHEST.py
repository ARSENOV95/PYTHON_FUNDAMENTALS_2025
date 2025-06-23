def valid_index(idx: int, seq: list) -> bool:
    return idx in range(len(seq))

initial_loot = input().split("|")
len_of_all_loot = 0

while True:
    command = input()

                
    if command == "Yohoho!":     
        print(", ".join(stolen_items))   

        if initial_loot:
            treasure_value = sum(map(lambda x: len(x), initial_loot))
            average = treasure_value / len(initial_loot)

            print(f"Average treasure gain: {average:.2f} pirate credits.")
        else:
            print("Failed treasure hunt.")
        break

    text, *args = command.split()

    if text == "Loot" and len(args) > 0:
        for arg in args:
            if arg not in initial_loot:
                initial_loot.insert(0, arg)

    elif text == "Drop":
        index = int(args[0])
        if not valid_index(index, initial_loot):
            continue

        removed_item = initial_loot.pop(index)
        initial_loot.append(removed_item)

    elif text == "Steal":
        steal_count = int(args[0])  # number of items to steal example 3

        if steal_count > len(initial_loot):
            stolen_items = initial_loot.copy()  # if number of items then clear the list
            initial_loot.clear()


        stolen_items = initial_loot[
                       -steal_count:]  # counts ofrm the enf of the list backowrds meaning 3 elements fro mthe last one - 7,6,5
        del initial_loot[-steal_count:]








