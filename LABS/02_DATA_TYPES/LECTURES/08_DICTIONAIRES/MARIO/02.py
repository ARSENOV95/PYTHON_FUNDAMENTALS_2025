stock_data = input().split()

products = {}

for  i in range(0,len(stock_data),2):
    product = stock_data[i]
    quantity = stock_data[i +1]

    products[product] = int(quantity)

products_to_search = input().split()

for item in products_to_search:
    if item in products.keys():
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

