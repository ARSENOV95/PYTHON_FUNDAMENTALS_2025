num_rows = int(input())

grid = []
destroyed_ships = 0

for i in range(num_rows):
    coordinates = list(map(int,input().split()))

    grid.append(coordinates)

#print(grid)

attacks = input().split()

print(attacks)

for attack in attacks:
    x,y = map(int,attack.split("-"))
    print(x,y)
    