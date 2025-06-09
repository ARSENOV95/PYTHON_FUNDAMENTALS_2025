def is_perfect(some_number :int) ->str:
    devisors_sum = 0

    for devisor in range(1,some_number):
        if some_number % devisor == 0:
            devisors_sum += devisors_sum


    if devisors_sum == some_number:
        return "We have a perfect number"  #when the if clause is true the return will execute and the rest of the program will not complete
    return "It's not so perfect." #when the if clause is false, then the row will be skipped 
                       
                                    


number = int(input())

print(is_perfect(number))