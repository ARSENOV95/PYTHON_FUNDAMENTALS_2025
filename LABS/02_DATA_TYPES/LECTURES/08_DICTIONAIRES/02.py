list_of_items = input().split()
requested_items = input().split()

products = {}

for  i in range(0,len(list_of_items),2):
    key = list_of_items[i]
    value = list_of_items[i +1]

    products[key] = int(value)


for item in requested_items:
    if item in products.keys():
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")


