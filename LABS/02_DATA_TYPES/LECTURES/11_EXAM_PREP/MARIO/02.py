import re
n = int(input())

barcode_pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(n):
    barcode = input()
    match = re.match(barcode_pattern,barcode)

    if match:
        core = match.group(1)
        product_group = ''

        product_grpup = ''.join(filter(str.isdigit,core))
        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    