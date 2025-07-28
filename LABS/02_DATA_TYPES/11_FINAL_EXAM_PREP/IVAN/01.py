def add_stop(stops_string :str,some_index :int,some_sub_string :str):
    if some_index in range(len(stops_string)):
        stops_string = stops_string[:some_index] + some_sub_string + stops_string[index:]
    return stops_string

def remove_stop(stops_string:str,some_start_index:int,some_end_index:int):
    if some_start_index in range(len(stops_string)) and some_end_index in range(len(stops_string)):
       stops_string[:some_start_index] + stops_string[some_end_index:]
    return stops_string


def switch(some_stops:str,some_old_string:str,some_new_string:str):
    if some_old_string in some_stops:
        some_stops = some_stops(some_old_string,some_new_string)
    return some_stops


stops = input()

command = input().split(":")

while command[0] != "Travel":
    if command[0] == 'Add Stop':
        index,sub_string = command[1],command[2]
        stops = add_stop(stops,index,sub_string)

    if command[0] == 'Remove':
        start_index,end_index = map(int,command[1:])
        stops = remove_stop(stops,start_index,end_index)

    if command[0] == 'Switch':
        old_string,new_string = command[1],command[2]
        stops = switch(stops,old_string,new_string)

    print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")