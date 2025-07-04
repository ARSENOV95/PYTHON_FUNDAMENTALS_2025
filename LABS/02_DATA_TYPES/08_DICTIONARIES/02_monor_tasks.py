count = 0
items = {}
list_of_items = []

while (string := input()) != 'stop':
    list_of_items.append(string)

for i in range(1,len(list_of_items)+1,2):
    key = list_of_items[i]
    value = int(list_of_items[i+1])

    if key not in items:
        items[key] = 0

    items[key] +=  value
        

for key,value in items.items():
    print(f"{key} -> {items}")