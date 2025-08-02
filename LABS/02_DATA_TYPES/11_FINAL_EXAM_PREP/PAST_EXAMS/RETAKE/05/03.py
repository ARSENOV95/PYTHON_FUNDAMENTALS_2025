stock = {}

sold_goods = 0

while (command := input()) != "Complete":
    action,quantity,food = command.split()
    quantity = int(quantity)

    match action:
        case "Receive":
            if quantity <= 0:
                continue

            if food not in stock.keys():
                stock[food] = quantity
            else:
                stock[food] += quantity
        
        case "Sell":
            if food not in stock.keys():
                print(f"You do not have any {food}.")
                continue

            if quantity >  stock[food]:
                print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
                sold_goods += stock[food]
                del stock[food]
            else:
                stock[food] -= quantity
                sold_goods += quantity
                print(f"You sold {quantity} {food}.")
                if stock[food] == 0:
                    del stock[food]


for food,quantity in stock.items():
    print(f"{food}: {quantity}")

print(f"All sold: {sold_goods} goods")


