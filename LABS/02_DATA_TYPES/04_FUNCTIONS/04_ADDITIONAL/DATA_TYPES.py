def data_types(data,val):
    if data == 'int':
        return int(val) * 2
    elif data == 'real':
        return f"{int(val)  * 1.5:.2f}"
    elif data == 'string':
        return f"${val}$"
    else:
        return ("Invalid data type")





data_type = input()
value = input()

print(data_types(data_type,value))