row_one = list(map(int,input().split()))
row_two = list(map(int,input().split()))
row_three = list(map(int,input().split()))

if row_one.count(1)  == 3 or row_two.count(1) == 3 or row_three.count(1) == 3 or\
    (row_one[0] == 1 and  row_two[0] == 1 and row_three[0] == 1) or\
    (row_one[1] == 1 and  row_two[1] == 1 and row_three[1] == 1) or\
    (row_one[2] == 1 and  row_two[2] == 1 and row_three[2] == 1) or\
    (row_one[0] == 1 and  row_two[1] == 1 and row_three[2] == 1) or\
    (row_one[2] == 1 and  row_two[1] == 1 and row_three[0] == 1):
    print("First player won")
elif row_one.count(2)  == 3 or row_two.count(2) == 3 or row_three.count(2) == 3 or\
    (row_one[0] == 2 and  row_two[0] == 2 and row_three[0] == 2) or\
    (row_one[1] == 2 and  row_two[1] == 2 and row_three[1] == 2) or\
    (row_one[2] == 2 and  row_two[2] == 2 and row_three[2] == 2) or\
    (row_one[0] == 2 and  row_two[1] == 2 and row_three[2] == 2) or\
    (row_one[2] == 2 and  row_two[1] == 2 and row_three[0] == 2):
    print("Second player won")
else:
    print("Draw!")