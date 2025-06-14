def check_happiness(happyness_lst,factor):

    improved_happiness = [cur_val * factor for cur_val in happyness_lst]
    avg_happiness  = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(num > avg_happiness for num in improved_happiness)
    total_count = len(improved_happiness)

    message = "happy" if  happy_count >=  total_count /2 else "not happy"

    return f"Score: {happy_count}/{total_count}.\nEmployees are {message}!"

    
happiness_lst = list(map(int,input().split()))
happiness_factor = int(input())


result = check_happiness(happiness_lst,happiness_factor)
print(result)