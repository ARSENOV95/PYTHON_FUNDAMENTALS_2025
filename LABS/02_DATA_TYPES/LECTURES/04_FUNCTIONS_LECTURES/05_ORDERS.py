def item_menue(item = input()): #we define the type of product directly in the funtion
    #we sue several logical condtions and for each we will return a value for each product
    if  item == "coffee":
        item_price = 1.50
        return item_price
    elif  item == "water":
        item_price = 1.00
        return item_price
    
    elif  item == "coke":
        item_price = 1.40
        return item_price

    elif  item == "snacks":
        item_price = 2.00
        return item_price

quantity_of_products = int(input()) #we input the quantity fo desired items

order_price = lambda price,quantity:  price * quantity #we use a lambda function to calcuate the final order 
print(f'{order_price(item_menue(),quantity_of_products):.2f}')