from math import floor

def center_point(x1 :float,y1 :float,x2 :float,y2 :float)->str:

    x1_abs = abs(x1)
    y1_abs = abs(y1)
    x2_abs = abs(x2)
    y2_abs = abs(y2)

    if (x1_abs + y1_abs) > (x2_abs + y2_abs):
        return f"({x2}, {y2})"
    elif (x1_abs  +  y1_abs) <= (x2_abs + y2_abs):
        return f"({x1}, {y1})"     

x_1 = floor(float(input()))
y_1 = floor(float(input()))
x_2 = floor(float(input()))
y_2 = floor(float(input()))

print(center_point(x_1,y_1,x_2,y_2))