def loading_bar(some_number :int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    
    loaded_percent = some_number//10
    return f"{some_number}% [{'%' * loaded_percent}{'.'*(10 - loaded_percent)}]\nStill loading..."
           #this will return an f string where the oading bar will be a string, and the symbols will be
           #% =  '%' * the loaded percentages
           #. = '.' * 10 -loaded perecntages which will multiply it exacly that many times needed until 10 symobls 


number = int(input())
print(loading_bar(number))