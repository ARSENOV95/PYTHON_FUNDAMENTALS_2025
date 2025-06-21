maze_levels = int(input())

current_level = 0
no_eskape = False

for level in range(maze_levels):
    current_level += 1

    layour = input()

    level_layout = [char for char in layour]
    if current_level > 1 and level_layout.count('#') == 6:
        no_eskape = True

    


if no_eskape:
    print("Kate cannot get out")
