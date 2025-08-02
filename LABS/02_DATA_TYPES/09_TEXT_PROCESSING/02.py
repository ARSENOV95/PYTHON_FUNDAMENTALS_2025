def difference_str(str1 :str,str2 :str,lst :list):
    diff = len(str1) - len(str2)
    additional = str1[-diff:]

    for chr in additional:
        lst.append(ord(chr))
    
    return lst

first_string,second_string = input_string = input().split()

result = [] #list to store the reult


if len(first_string) == len(second_string): #when both strings are the same leght we multiply each elemt to the toher 
    result = [ord(first_string[i]) * ord(second_string[i])  for  i in range(len(first_string))]

elif len(first_string) > len(second_string): #when the lengs are different we muliply each elemento form both string where the lght is the smaller elemrnt 
    result = [ord(first_string[i]) * ord(second_string[i])  for  i in range(len(second_string))] 
    difference_str(first_string,second_string,result)

else:
    result = [ord(first_string[i]) * ord(second_string[i])  for  i in range(len(first_string))] 
    difference_str(second_string,first_string,result)

print(sum(result))
