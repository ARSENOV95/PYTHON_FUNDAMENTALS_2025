def check_index_validity(idx :int,string :str)->bool:
    return  0 <= idx < len(string)

stops = input()

while (command := input()) != 'Travel':
    actions = command.split(':')
    action = actions[0]

    match action:
        case 'Add Stop':
            index,string = map(str,actions[1:])
            index = int(index)
            if check_index_validity:
               stops = stops[:index] + string + stops[index:]

        case 'Remove Stop':
            start_index,end_index = map(int,actions[1:])
            #check index validity - valid if start < end and both are in the string range
            if start_index <= end_index and 0<= start_index < len(stops) and 0<= end_index < len(stops):
                stops = stops[:start_index] + stops[end_index+1:]

        case 'Switch':
            old_string,new_string = map(str,actions[1:])
            stops = stops.replace(old_string,new_string)
    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")