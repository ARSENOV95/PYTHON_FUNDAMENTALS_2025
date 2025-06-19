target_sequence = [int(num) for num in  input().split()]

while True:
    index = input()

    if index == "End":
        break
    target_index = int(index)

    if target_index not in range(len(target_sequence)):
        continue

    if  target_sequence[target_index] == -1:
        continue
    
    shot_target = target_sequence[target_index]
    target_sequence[target_index] = -1

    for target in range(len(target_sequence)):
        if target_sequence[target] == -1:
            continue

        if target_sequence[target] > shot_target:
            target_sequence[target] -= shot_target
        elif target_sequence[target] <= shot_target:
            target_sequence[target] += shot_target

    

print(f'Shot targets: {target_sequence.count(-1)} -> {" ".join([str(el) for el in target_sequence])}')


