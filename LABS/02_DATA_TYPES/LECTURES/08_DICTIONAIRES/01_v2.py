initial_list = input().split()

keys = []
values = []
stock = {}

for item in range(0,len(initial_list),2):
    food = initial_list[item]
    quan = int(initial_list[item + 1])
    stock[food] = quan


print(stock)