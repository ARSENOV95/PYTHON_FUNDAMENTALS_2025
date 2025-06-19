total_price = 0
is_special = False

while True:
    component_price = input()

    if component_price == 'special' or  component_price == 'regular':
        if component_price == 'special':
            is_special = True
        break

    price = int(component_price)

    if price <= 0:
       print("Invalid price!")
       continue
        
    total_price += price

if total_price == 0:
    print("Invalid order!")
else:
    if is_special:
        total_price -= total_price * 0.10
        taxes = total_price * 0.20

        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price}$")
        print(f"Taxes: {taxes}$")
        print(f"Total price: {total_price + taxes}$")
