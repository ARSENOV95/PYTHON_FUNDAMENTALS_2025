def cheat_check(idx_1 :int,idx_2 :int,seq :list)->bool:                                         #function to check if the endered idnexes are valid
   return idx_1 != idx_2 or (idx_1 in range(len(seq)) and idx_2 in range(len(seq)))

def index_val_check(idx1 :int,idx2 :int, lst :list)->bool:  #funtico to check if the values at the given indexes are equal
    return lst[idx1] == lst[idx2]

sequence_of_indexes = input().split()

turn_number = 0

while True:
    player_input = input()


    if player_input == "end":   #if the programs is ended we check if the sequence is empty if not we print the current state
        print("Sorry you lose :(")
        print(f'{" ".join(sequence_of_indexes)}')
        break

    turn_number += 1  #if input != end we increase the turn number as we start a new turn

    index1,index2 = player_input.split()  #we split the input into two indexes
    index1 = int(index1)
    index2 = int(index2)

    if not cheat_check(index1,index2,sequence_of_indexes):   #we chec if the indexes are valid
        print("Invalid input! Adding additional elements to the board")
        sequence_of_indexes.insert(len(sequence_of_indexes) // 2, f"-{turn_number}a")
        sequence_of_indexes.insert(len(sequence_of_indexes) // 2, f"-{turn_number}a")

    elif index_val_check(index1,index2,sequence_of_indexes):
       print(f"Congrats! You have found matching elements - {sequence_of_indexes[index1]}!") #if valid we check if they match
       sequence_of_indexes.pop(max(index1,index2))
       sequence_of_indexes.pop(min(index1,index2))

    elif not index_val_check(index1,index2,sequence_of_indexes): #if they do not match we print a message and continue
        print("Try again!")


    if not sequence_of_indexes: #if the sequence is empty we won the game and exit the loop
        print(f"You have won in {turn_number} turns!")
        break



