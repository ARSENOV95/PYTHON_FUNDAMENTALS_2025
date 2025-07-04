list_of_items = []
all_items = {}

while (item := input()) != 'stop':
    list_of_items.append(item)

for i in range(0,len(list_of_items),2):
    key = list_of_items[i]
    value = int(list_of_items[i + 1])

    if key not in all_items:
        all_items[key] = 0
    all_items[key] += value


for key,value in all_items.items():
    print(f"{key} -> {value}")
