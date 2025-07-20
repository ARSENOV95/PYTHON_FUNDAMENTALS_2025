import re

total_income = 0

while (string := input()) != "end of shift":
    pattern = r"\%([A-Z][a-z]+)\%[^|%$.]*?<(\w+)>[^|%$.]*?\|(\d+)\|[^$%.]*?(\d+(?:\.\d+)?)\$"

    match = re.match(pattern,string)
    if match:
        name,product,quantity,price = match.groups()
        order = float(price) * int(quantity)
        total_income += order

        print(f"{name}: {product} - {order:.2f}")

print(f"Total income: {total_income:.2f}")