resourses = {}

while True:
    current_resource = input()

    if current_resource == "stop":
        break

    current_quantity = int(input())

    if current_resource not in resourses.keys():
        resourses[current_resource] = 0
    resourses[current_resource] += current_quantity


for res,quan in resourses.items():
    print(f"{res} -> {quan}")