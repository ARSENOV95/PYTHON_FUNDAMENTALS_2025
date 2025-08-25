from math import floor

def line_checker(x1 :float,y1 :float,x2 :float,y2 :float,x3 :float,y3 :float,x4 :float,y4 :float)->str:
    line1 = abs(x1) + abs(x2) + abs(y1)- abs(y2) 
    line2 = abs(x3) + abs(x4) + abs(y3)- abs(y4)    

    if line1 >= line2:
        return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
    elif line2 > line1:
        return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"    


l1_x1 = float(input())
l1_y1 = float(input())
l1_x2 = float(input())
l1_y2 = float(input())

l2_x1 = float(input())
l2_y1 = float(input())
l2_x2 = float(input())
l2_y2 = float(input())

print(line_checker(l1_x1,l1_y1,l1_x2,l1_y2,l2_x1,l2_y1,l2_x2,l2_y2))