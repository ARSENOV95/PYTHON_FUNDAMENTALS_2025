import re 

phone = '0876292882'

pattern_phone = r'^08[7-9]\d{7}'


if re.match(pattern_phone,phone):
    print(f"{phone} is ")
else:
    print(f"{phone} is not valid")