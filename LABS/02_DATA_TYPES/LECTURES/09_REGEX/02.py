import re

number = input()

pattern = "(\+359-2-[0-9]{3}-[0-9]{4}\\b|\+359 2 [0-9]{3} [0-9]{4})\\b"
match = re.findall(pattern,number)
print(", ".join(match))

