def check_happiness(happyness_lst,factor):

    improved_happiness = [cur_val * factor for cur_val in happyness_lst]
    avg_happiness  = sum(improved_happiness) / len(improved_happiness)

    happy = list(filter(lambda x: x > avg_happiness,improved_happiness))

    if len(happy) < len(improved_happiness):
        return f"{len(happy)}/{len(improved_happiness)}.\n Employees are not happy!"
    
    return f"{len(happy)}/{len(improved_happiness)}.\n Employees are happy!"

happiness_lst = list(map(int,input().split()))
happiness_factor = int(input())


result = check_happiness(happiness_lst,happiness_factor)
print(result)