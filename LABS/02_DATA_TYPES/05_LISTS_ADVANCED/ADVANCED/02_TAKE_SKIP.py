#def_check if index is out of rang

def validation_range(num :int,seq):
    return num <= len(seq)

#function for intial list split
def list_split(init :list,num_lst :list,str_lst :list)->list:
    for chr in init:
        if chr.isnumeric():
            num_lst.append(int(chr))
        else:
            str_lst.append(chr)

    return string_list,numeric_list

#function for splitting the nubewrs into even or odd
def even_odd(nums :list,evn :list,odd :list)->list:
    for idx in range(len(nums)):
        if idx %2 == 0:
            evn.append(nums[idx])
        else:
            odd.append(nums[idx])
    return evn,odd

#intial input
intial_string = input()
string_list = []
numeric_list = []
even_nums = []
odd_nums = []

list_split(intial_string,numeric_list,string_list)
even_odd(numeric_list,even_nums,odd_nums)

final = []

for index in range(len(even_nums)):

    if even_nums[index] == 0:
        items_to_skip = odd_nums[index]
        if items_to_skip > 0:
            del string_list[:items_to_skip]
        continue

    items_to_add = even_nums[index]

    #if not validation_range(items_to_add,string_list):
        #continue
 
    final += string_list[:items_to_add]

    del string_list[:items_to_add]

    items_to_skip = odd_nums[index]
    if items_to_skip > 0:
        del string_list[:items_to_skip]
    
if (final[-1]) == " ":
    final.pop(-1)

print("".join(final))


    