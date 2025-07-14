input_string = input()
emoji = []

for index in range(len(input_string) - 1):
    if input_string[index].startswith(":"):
        print(f":{input_string[index+1]}")

