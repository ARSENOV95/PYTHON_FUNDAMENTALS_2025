import re


bought_frurniture = []
total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)'

command = input()

while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        item,price,quantity = match.groups()
        bought_frurniture.append(item)
        total_cost += float(price) * int(quantity)

    command = input()


print("Bought furniture:")
print("\n".join(bought_frurniture))
print(f"Total money spend: {total_cost:.2f}")

