force_side_dicitonary = {}

command = input()

while command != 'Lumpawaroo':
    if "|" in command:
        force_side,force_user = command.split(" | ")
        force_user_is_part_of_the_force = False
        for  list_with_force_users in force_side_dicitonary.values():
            if force_user in list_with_force_users:
                force_user_is_part_of_the_force = True
                break
        
        if not force_user_is_part_of_the_force:
            if force_side not in force_side_dicitonary.keys():
                force_side_dicitonary[force_side] = []
            force_side_dicitonary[force_side].append(force_user)

    
    elif "->" in command:
        force_user,force_side = command.split(" -> ")
        force_user_is_part_of_the_force = False
        for  list_with_force_users in force_side_dicitonary.values():
            if force_user in list_with_force_users:
                list_with_force_users.remove(force_user)
                break
        if force_side not in force_side_dicitonary.keys():
            force_side_dicitonary[force_side] = []
        force_side_dicitonary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()


for force_side, list_with_force_users  in  force_side_dicitonary.items():
    if list_with_force_users:
        print(f"Side: {force_side}, Members: {len(list_with_force_users)}")
        for force_user in list_with_force_users:
            print(f"! {force_user}")