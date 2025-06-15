current_version = list(map(int,input().split(".")))

if current_version[-1] in range(0,9):
    current_version[-1] += 1
else:
    if current_version[-1] == 9 and current_version[-2] < 9:
        current_version[-1] = 0
        current_version[-2] += 1
    elif current_version[-1] == 9 and current_version[-2] == 9:
        current_version[-1] = 0
        current_version[-2] = 0
        current_version[0] += 1

next_version = [str(string) for string in current_version]

print(".".join(next_version))
        