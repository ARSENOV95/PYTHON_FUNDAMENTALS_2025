ticket_price = 150

item_price_markup = 0.40

items_to_buy =  input().split("|")
budget = int(input())

sum_items_bought = 0
sum_items_sold = 0
sold_items = list()

if budget <= 0:
     quit()

for item in items_to_buy:
     item_attributes = item.split("->")
     item_type = item_attributes[0]
     item_price = float(item_attributes[1]) 


     if item_price > budget or\
        ((item_type == "Clothes" and item_price >= 50.00) or\
        (item_type == "Shoes" and item_price >= 35.00) or\
        (item_type == "Accessories" and item_price >= 20.50)):
        continue
     
     else:
        sum_items_bought += item_price
        budget -= item_price

        new_price = item_price + (item_price * item_price_markup)
        sum_items_sold += new_price
        sold_items.append(f"{new_price:.2f}")

profit = sum_items_sold - sum_items_bought


print(f"{" ".join(sold_items)}\nProfit: {profit:.2f}")

if (sum_items_sold + budget) >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")






