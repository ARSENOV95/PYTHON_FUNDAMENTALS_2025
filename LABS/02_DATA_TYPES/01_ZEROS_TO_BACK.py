a_list_of_numbers = input().split(", ") #enter a stirng of numbers separated by ", " and append them tyo a list split by ", "

a_list_of_numbers = [int(integer) for integer in a_list_of_numbers] #convert every element of the list to an integer 

final_list = [] #create one list to store the final outlook of the list 

zero_count = a_list_of_numbers.count(0) #counts how may times the element 0 is in  the list 


for number in a_list_of_numbers: #for ever y number i nthe list 
    if number != 0: #check if != 0 and append it ot the list 
        final_list.append(number)

#Why??? because in python loops do not accoutn for change in list lenght if you have 1 0 1 0:
#After itration 2 0 lets say is popped out of the list, then thel ist will be  110 or indexes  012,
#while the iteratinos go on 0 will be skipped

final_list.extend([0] * zero_count) #as  final reuslt we have the non zero list and extedn it by [O] elements * the cout of zeros = 2
print(final_list)

