number_of_integers = input().split( )  #we input a single string of numbers separated by a " " ans split it inot a list of elemnts (all string)
numbers_to_remove = int(input())     #count of how many numbers form min to max to be removed 


numbers_sorted  = [int(number) for number in number_of_integers]

for current_number in range(numbers_to_remove):
    numbers_sorted.sort(reverse=True)
    del numbers_sorted[-1]

result = ", ".join(map(str,numbers_sorted))
print(result)