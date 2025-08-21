#def valid_coordinates(row :int, column :int)->bool:


num_rows = int(input())

grid = []


destroyed_ships = 0

for i in range(num_rows):
    coordinates = list(map(int,input().split()))

    grid.append(coordinates)

#print(grid)



attacks = input().split()

#print(attacks)

for i in range(len(attacks)):
    x,y = map(int,attacks[i].split("-"))

    if grid[x][y] > 0:
        grid[x][y] -= 1 
        if grid[x][y] == 0:
            destroyed_ships += 1


print(destroyed_ships)
