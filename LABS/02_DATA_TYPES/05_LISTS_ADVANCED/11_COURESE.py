list_of_coureses = input().split(",")

while (command := input()) != "course start":
    instruction,*args = command.split(":")
    course = args[0]
    index = int(args[1]) if len(args) > 1 else 0

    if course not in list_of_coureses:
        if instruction == "Add":
            list_of_coureses.append(course)
        elif instruction == "Insert":
            list_of_coureses.insert(index,course)

    elif course in list_of_coureses:
        if instruction == "Remove":
            list_of_coureses.remove(course)
            if course+"-Exercise" in list_of_coureses:
                list_of_coureses.remove(course+"Exercise")




