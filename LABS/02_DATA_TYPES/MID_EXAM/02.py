def index_validity(idx :int, seq :list)->bool:
    return 0<= idx <len(seq)

usernames = input().split(", ")

blacklist = []
lost = []

while (command := input()) != "Report":
    args = command.split()[1:]

    if command.startswith("Blacklist"):
        name = args[0]

        if name not in usernames:
            print(f"{name} was not found.")
            continue

        name_idx = usernames.index(name)
        backlisted_name = usernames[name_idx]
        usernames[name_idx]  = "Blacklisted"

        print(f"{backlisted_name} was blacklisted.")
        blacklist.append(backlisted_name)

    elif command.startswith("Error"):
        index = int(args[0])
        if not (index_validity(index,usernames) and (usernames[index] != "Blacklisted" and usernames[index] != "Lost")):
            continue

        lost_name = usernames[index]
        usernames[index] = "Lost"
        print(f"{lost_name} was lost due to an error.")
        lost.append(lost_name)

    elif command.startswith("Change"):
        index = int(args[0])
        new_name = args[1]

        if not index_validity(index,usernames):
            continue

        current_name = usernames[index]
        print(f"{current_name} changed his username to {new_name}.")
        usernames[index] = new_name


print(f"Blacklisted names: {len(blacklist)} ")
print(f"Lost names: {len(lost)}")
print(" ".join(usernames))
