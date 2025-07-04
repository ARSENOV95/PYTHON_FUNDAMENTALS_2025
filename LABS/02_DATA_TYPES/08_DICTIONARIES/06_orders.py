product_prices = {}

#product_prices = {"beer":2,20...}

while True:
    product_date = input()
    
    if product_date == "buy":
        break

    product,price,quantity = product_date.split(" ")
    price = float(price)
    quantity = int(quantity)

    if product not in product_prices:
        product_prices[product] = [0,0] 
    product_prices[product][0] = price     
    product_prices[product][1] += quantity
    

for product,price_quan in product_prices.items():
    total_price = price_quan[0] * price_quan[1]
    print(f"{product} -> {total_price:.2f}")





