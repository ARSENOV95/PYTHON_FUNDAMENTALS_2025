inital_list = input().split()

keys = []
values = []

for item in range(len(inital_list)):
    if item % 2 == 0:
        keys.append(inital_list[item])
    else:
        values.append(int(inital_list[item]))

dictionary = dict(zip(keys,values))

print(dictionary)