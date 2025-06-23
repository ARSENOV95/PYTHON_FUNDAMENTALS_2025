def check_skip(pos :int,hood :list)->bool:
    return pos in range(len(hood))

neigbourhood = list(map(int,input().split('@')))
 
last_postion = 0
 
while (command := input()) != 'Love!':
    command_text,index = command.split()
 
    index = int(index)
 
    curr_positon = last_postion + index
 
    if not check_skip(curr_positon,neigbourhood):
       curr_positon = 0
 
    if neigbourhood[curr_positon] !=  0:
        neigbourhood[curr_positon] = neigbourhood[curr_positon] - 2
        if neigbourhood[curr_positon] == 0:
           print(f"Place {curr_positon} has Valentine's day.")
 
    elif neigbourhood[curr_positon] == 0:
        print(f"Place {curr_positon} already had Valentine's day.")
 
    last_postion = curr_positon
 
print(f"Cupid's last position was {last_postion}.")
 
if sum(neigbourhood) == 0:
    print("Mission was successful.")	
else:
    print(f"Cupid has failed {len(neigbourhood) - neigbourhood.count(0)} places.")