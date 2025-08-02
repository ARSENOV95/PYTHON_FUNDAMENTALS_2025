def exchange(idx :int,lst :list)->list:
    fist_half = lst[:idx +1]
    second_half = lst[idx +1:]
    lst = second_half + fist_half
    return lst

intial_list = (list(map(int,input().split())))


while (command := input()) != 'end':
    parts = command.split()

    action = parts[0]
    match action:
        case 'exchange':
            index = int(parts[1])
            if index < 0 or index >= len(intial_list):
                print("Invalid index")
                continue

            intial_list = exchange(index,intial_list)

        case 'max'|'min':
            defintion = parts[1]
            even_lst = list(filter(lambda x: x %2 == 0,intial_list))
            odd_lst = list(filter(lambda x: x %2 != 0,intial_list))
  
           