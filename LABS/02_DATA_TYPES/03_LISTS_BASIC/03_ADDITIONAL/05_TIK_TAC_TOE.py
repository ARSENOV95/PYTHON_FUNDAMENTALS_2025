first_row = [int(element) for element in input().split()]
second_row = [int(element) for element in input().split()]
third_row = [int(element) for element in input().split()]


full_grid = first_row + second_row + third_row
if (full_grid[0] + full_grid[1]+ full_grid[2]) == 3 or\
   (full_grid[3] + full_grid[4]+ full_grid[5]) == 3 or\
   (full_grid[6] + full_grid[7]+ full_grid[8]) == 3 or\
   (full_grid[0] + full_grid[3]+ full_grid[6]) == 3 or\
   (full_grid[1] + full_grid[4]+ full_grid[7]) == 3 or\
   (full_grid[2] + full_grid[5]+ full_grid[8]) == 3 or\
   (full_grid[0] + full_grid[5]+ full_grid[8]) == 3 or\
   (full_grid[0] + full_grid[4]+ full_grid[8]) == 3 or\
   (full_grid[2] + full_grid[4]+ full_grid[6]) == 3:
   print("First player won")

elif (full_grid[0] + full_grid[1]+ full_grid[2]) == 6 or\
     (full_grid[3] + full_grid[4]+ full_grid[5]) == 6 or\
     (full_grid[6] + full_grid[7]+ full_grid[8]) == 6 or\
     (full_grid[0] + full_grid[3]+ full_grid[6]) == 6 or\
     (full_grid[1] + full_grid[4]+ full_grid[7]) == 6 or\
     (full_grid[2] + full_grid[5]+ full_grid[8]) == 6 or\
     (full_grid[0] + full_grid[5]+ full_grid[8]) == 6 or\
     (full_grid[0] + full_grid[4]+ full_grid[8]) == 6 or\
     (full_grid[2] + full_grid[4]+ full_grid[6]) == 6:
     print("Second player won")
