row_nums = int(input()) #intial number of rows

count_dots = 0 #varable to store all connected dots

grid = [] #store the results from the prev row for lookup



for row in range(row_nums):
    current_row = input().split()
    grid.append(current_row)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == grid[i][j]

    