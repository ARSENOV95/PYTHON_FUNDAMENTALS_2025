def memory_game():
    sequence_data = input().split()

    while (command := input()) != "end":
        total_moves = 0 
        indexes = command.split()

        match indexes:
            case [index1,index2] if index1.isdigit() and index2.isdigit():
                in1,in2 = int(index1), int(index2)

                match (in1 == in2 or in1 not in range(len(sequence_data)) or\
                       in2 not in range(len(sequence_data))):
                    case True:
                        middle_index = len(sequence_data) // 2
                        elem = f"-{total_moves}a"
                        sequence_data[middle_index:middle_index] = [elem, elem]
                        print("Invalid input! Adding additional elements to the board")
                    
                    case False if sequence_data[in1] == sequence_data[in2]:
                        element = sequence_data[in1]
                        print(f"Congrats! You have found matching elements - {element}!")

                        for i in  sorted([in1, in2], reverse=True):
                            sequence_data.pop(i)

                    case False:
                        print("Try again!")

        if not sequence_data:
            print(f"You have won in {total_moves} turns!") 
            return