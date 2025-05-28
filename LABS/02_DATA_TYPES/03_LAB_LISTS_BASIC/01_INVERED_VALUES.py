string = input()

string_list = string.split()
converted_list = []

for string in string_list:
    if string == '0':
        converted_list.append(0)
   
    elif string.startswith("-"):
        string = string.replace("-","")
        converted_list.append(int(string))
    else:
        converted_list.append(int(f"-{string}"))


print(converted_list)
