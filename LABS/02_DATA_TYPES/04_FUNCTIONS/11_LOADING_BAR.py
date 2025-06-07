percentage = int(input())

def percentage_bar(percent):

    if percentage < 0 or percentage > 100:  #initial check of invalid percentage is entered
        print("Invalid percentage")
        quit() #quit the program if invalid percentage is entered 

    percentages = percentage // 10 #
    result = ""

    bar = ["[",".",".",".",".",".",".",".",".",".",".","]"] 
    # a list to holld all symbols in a bar first and las - [],  
    # 10 . as placeholder for every % sign 

    for index in range(1,percentages + 1):   #for each itteration form 1 the very 10% percent check every symbol in the bar
        if bar[index] == ".": #if symbol = ., replace with %
            bar[index] = '%'


    if percentage < 100:
        result = f"{percentage}% " + "".join(bar) + "\nStill loading..." 
 
    else:
        result = f"{percentage}% " f"Complete!\n" + "".join(bar)

    return result

print(percentage_bar(percentage))
    