rounded_list = []

list_of_strings = input().split(" ")

def rounding(list):

    for item in list:
        number = round(float(item))
        rounded_list.append(number)
    return rounded_list


print(rounding(list_of_strings))

