list_of_strings = input().split(', ') #we neter a string input 
#lookup_string = input()
lookup_string = input()


strings_ins_second_string = [string for string in list_of_strings if string in lookup_string]
print(strings_ins_second_string)

#in python we checking if a string from a lsit is in another list it wont work as 
#list to list comaprison or lookup is direct
#  list = ["cat"] list2 = ["concat"]  list3 = []
#  for element in list:
#      if element in list2
#        list3.append(element) ##list3 = []

#correct way:
#lookup_string = input().split(', ') 
#list3 = []

#for string in list_of_strings:
#    for item  in lookup_string:
#        if string in item:
#            list3.append(string)
#
#final = set(list3)
#print(final)