import re

total_income = 0
orders = {}


while (string := input()) != "end of shift":
    pattern = r"\%([A-Z][a-z]+)\%[^|%$.]*?<(\w+)>[^|%$.]*?\|(\d+)\|[^$%.]*?(\d+(?:\.\d+))\$"

    
    match = re.match(pattern,string)
    if match:
        name,product,quantity,price = match.groups()
        order = float(price) * int(quantity)
        total_income += order

    if product not in orders:
        orders[name] = 0
    orders[name] = f"{product} - {order:.2f}"

for name,order_price in orders.items():
    print(f"{name}: {order_price}")

print(f"Total income: {total_income:.2f}")