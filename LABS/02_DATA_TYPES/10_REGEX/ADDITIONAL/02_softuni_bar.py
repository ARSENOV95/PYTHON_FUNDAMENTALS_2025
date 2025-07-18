import re

total_income = 0
orders = {}


while (string := input()) != "end of shift":
    pattern = r"(%([A-Z]{1}[a-z]+)%(?!\|\$\%\.)<(\w+)>\|(?!\|\$\%\.)(\d+)\|(?!\|\$\%\.)(\d+\.\d+)\$)"

    match = re.match(pattern,string)

    if match:
        name,product,count,price = match.groups()[1:]
        order_price = int(count) * float(price)
        total_income += order_price
        orders[name] =  f"{product} - {order_price:.2f}"


for name,order in orders.items():
   print(f"{name}: {order}")

print(f"Total income: {total_income:.2f}")