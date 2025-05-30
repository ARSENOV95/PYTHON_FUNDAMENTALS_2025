list_of_integers = list(map(int,input().split())) #takes an iinput consisting of severa numnbers in on string and maps them as integers  and palces them as elements in a list
numbers_to_remove = int(input()) #number of elements to be removed 


for number_removed in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

list_of_biggest = ", ".join(map(str,list_of_integers))

print(list_of_biggest)



