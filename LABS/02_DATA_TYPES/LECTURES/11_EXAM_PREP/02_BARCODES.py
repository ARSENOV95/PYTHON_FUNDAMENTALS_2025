import re

number_of_barcodes = int(input())

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for code in range(number_of_barcodes):
    
    bacode = input()
    product_group = ''

    valid_barcode = re.match(pattern, bacode)

    if valid_barcode:
        for char in valid_barcode.group():
            if char.isdigit():
                product_group += char
    else:
        print('Invalid barcode')
        continue


    print(f"Product group: {product_group}" if product_group else "Product group: 00")

