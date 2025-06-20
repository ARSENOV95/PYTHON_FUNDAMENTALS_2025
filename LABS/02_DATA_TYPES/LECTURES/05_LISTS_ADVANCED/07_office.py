def check_happiness(happyness_lst,factor):

    improved_happiness = [cur_val * factor for cur_val in happyness_lst]
    avg_happiness  = sum(improved_happiness) / len(improved_happiness)

    happy = len(list(filter(lambda x: x > avg_happiness,improved_happiness)))
    
    message = "happy" if happy >= len(improved_happiness) / 2 else "not happy"
    return f"Score: {happy}/{len(improved_happiness)}. Employees are {message}!"
    
happiness_lst = list(map(int,input().split()))
happiness_factor = int(input())

result = check_happiness(happiness_lst,happiness_factor)
print(result)