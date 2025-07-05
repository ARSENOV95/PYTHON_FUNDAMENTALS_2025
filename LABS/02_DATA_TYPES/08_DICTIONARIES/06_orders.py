product_prices = {}

#product_prices = {"beer":2,20...}

while True:  #while true enter the product data 
    product_date = input()
    
    if product_date == "buy": #if the input = buy end the program 
        break

    product,price,quantity = product_date.split(" ") #if not buy pars the program, lese break 
    price = float(price)
    quantity = int(quantity)

    if product not in product_prices:  #if a new product  create a list with 2 placeholder values 
        product_prices[product] = [0,0] 
    product_prices[product][0] = price    #to bypas adtinoal code increase the quantity of the product if exists with the new one 
    product_prices[product][1] += quantity #set the price to the newlone 
    

for product,price_quan in product_prices.items():
    total_price = price_quan[0] * price_quan[1]  
    print(f"{product} -> {total_price:.2f}") #print each itterated key, the price will be a byrpdocut of the quanity x price 





