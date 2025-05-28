list_of_numbers = [1,2,3,4,5]

copy_number_list = list_of_numbers.copy()
#print(copy_number_list)


#print(list_of_numbers.count(4)) #returns the count of the element in the list

index = list_of_numbers.index(4) #returns the index of the element in the list
#print(index) #printss the index of value 4

#index = list_of_numbers.index(2,2)
#print(index) #prints the index of value 2 starting from index 2


list_of_numbers.insert(2, 10) #inserts the value 10 at index 2
print(list_of_numbers) #prints the list after insertion

list_of_numbers.pop() #
print(list_of_numbers) #removes the last element of the list

list_of_numbers.pop(2) #removes the element at index 2
print(list_of_numbers) 

reversed = list_of_numbers.reverse() #reverses the list
print(list_of_numbers) #prints the list after reversing

removed = list_of_numbers.remove(2) #
print(removed)