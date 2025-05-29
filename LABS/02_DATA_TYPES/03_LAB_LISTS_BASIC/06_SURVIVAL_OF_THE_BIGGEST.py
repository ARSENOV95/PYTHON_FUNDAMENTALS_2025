import sys

list_of_integers = list(map(int,input().split()))
numbers_to_remove = int(input())



for number_removed in range(numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

list_of_biggest = ", ".join(map(str,list_of_integers))

print(list_of_biggest)



