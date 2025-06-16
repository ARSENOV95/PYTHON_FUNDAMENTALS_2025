from math import pow

number_of_electrons = int(input()) #inital variabe for given electrons 

layers = [] #an empty list to store the distributed electorns by layer
layer = 1 #variable to mark the intial layer

while sum(layers) < number_of_electrons: #while the sum of all distributre
    electron_distribution = 2 * pow(layer,2) # the electorns ditirbuted per layer =  2 * layer ** 2
    left_space_per_layer = number_of_electrons - sum(layers)  #variable to calculate the left space in the layers 

    if electron_distribution  > left_space_per_layer:  #if the space is not enoguh fo fit the whole 2* layer ** 2, then add the difference fro mthe current occupied layer the the total given electrons 
        layers.append(left_space_per_layer)
        continue

    layers.append(electron_distribution) #else appedn the formula

    layer += 1 #move to the next layer 

print(layers)

   