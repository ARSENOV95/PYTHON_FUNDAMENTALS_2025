numbers_input = list(map(int,input().split(", ")))
#takes a squence of strings representyed as a number and splits them i na list converted to numric type

list_of_even_numbers = list(map(lambda x: x if numbers_input[x] %2 == 0 else "None",range(len(numbers_input))))
#we sure the map fuction to create a niew list 
#we use lambda for the lenght of the list, checking evey index in hte lenght of  the list is  devisable by 2
#if the even then it will be added by tis value in the new list, if odd it will be added as none 

filed_list = list(filter(lambda x: x != 'None',list_of_even_numbers))

print(filed_list)

