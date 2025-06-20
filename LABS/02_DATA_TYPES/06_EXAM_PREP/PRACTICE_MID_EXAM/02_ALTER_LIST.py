def index_validity(idx1 :int,idx2 :int,seq :list):
    return idx1 in range(len(seq)) and idx2 in range(len(seq))

numbers_array = [int(el) for el in input().split()]

if not numbers_array:
    quit()

while True:
    command = input()

    if command == "end":
        print(", ".join([str(val) for val in numbers_array]))
        break 

    if command != "decrease":
        index1,index2 = command.split()[1:]

        index1 = int(index1)
        index2 = int(index2)

        if not (index_validity(index1,index2,numbers_array) and index1 != index2):
            continue
    
    if command.startswith("swap"):
        numbers_array[index1],numbers_array[index2] = numbers_array[index2],numbers_array[index1]

    elif command.startswith("multiply"):
        numbers_array[index1] = numbers_array[index1] * numbers_array[index2]

    elif command.startswith("decrease"):
        for index in range(len(numbers_array)):
            numbers_array[index] -= 1

