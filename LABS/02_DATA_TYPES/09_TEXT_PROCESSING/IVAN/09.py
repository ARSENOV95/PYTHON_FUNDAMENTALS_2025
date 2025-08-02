def rage_quit(series_of_stringa :str):
    unique = 0
    for index in range(len(series_of_stringa)):
        if series_of_stringa.count(series_of_stringa[index]) == 1:
            unique + 1


 


    return f"Unique symbols used {unique}"
 

strings = input()

print(rage_quit(strings))