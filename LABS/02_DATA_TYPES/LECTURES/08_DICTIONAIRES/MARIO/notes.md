keys = ['name','age','major']
values = ['Geprge',22,'Engineer']

dictiobnary = dict(zip(keys,values))

#the zip functions goups the elemenys from tuples and pairs thme in a set
the resulting pairs will be paired as keys and values 

print(dictiobnary.keys()) #prints all the keys
print(dictiobnary.values()) #prints all the values
print(dictiobnary.items()) #prints all th keys and values

####getting valuese by keys

my_dict['name'] #returns the value for key name
my_dict.get(name) #does the same 

#!!!! if a key is not found get will return None, [] will return error

####
my_dict.update({"occupation": 'engineer'}) #adds a new pair at the ned of the list

my_dict = {name: ['Gosho','Pesho','Ivan']}

for name in dict[name]  # if a value is a list we can itterate by the eky for tha t value
    print(name)

can