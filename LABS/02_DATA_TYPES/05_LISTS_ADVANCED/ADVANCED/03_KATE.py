number_of_levels = int(input())

maze = []
moves = 0
deadend = False

for level in range(number_of_levels):
    curr_lvl = input()
    maze.append(curr_lvl)


for lvl in range(1,len(maze)):
   level = maze[lvl]
   for i  in range(len(level)):
       #print(level[i])
       if not(level[i] == 'k' or level[i] == '#'):
           moves += 1
    
if moves >= number_of_levels:
    moves += 1 
    print(f'Kate got out in {moves} moves')
else:
    print('Kate cannot get out')
