stock = {}

while True:
    line = input()

    if line == "statistics":
        break

    product,quantity = line.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity

    else:
        stock[product] = quantity


prodcut_count = len(stock)
total_quantity = sum(stock.values())

print("Products in stock:")
for key in stock:
    print(f"- {key}: {stock.get(key)}")

print(f"Total Products: {prodcut_count}")
print(f"Total Quantity: {total_quantity}")