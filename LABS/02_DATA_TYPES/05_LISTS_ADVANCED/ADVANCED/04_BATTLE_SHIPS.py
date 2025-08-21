num_rows = int(input())

grid = []

for i in range(num_rows):
    coordinates = list(map(int,input().split()))

    grid.append(coordinates)

print(grid)

attackes = input().split()