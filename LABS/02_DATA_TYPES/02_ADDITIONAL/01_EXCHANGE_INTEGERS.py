a = int(input()) #5
b = int(input()) #10

c = a #0 >> 5
a = b #5 >> 10
b = c #10 >> 5

print(f"Before: \na = {b} \nb = {a} \nAfter: \na = {a} \nb = {c}")