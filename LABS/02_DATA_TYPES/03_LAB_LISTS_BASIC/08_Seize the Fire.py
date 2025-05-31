fire_cells = input().split("#") #input the fumber fo fire cells 
current_water_amount = int(input()) #total amaout of letf water for the party

effort = 0  #the total amount of efferdto be calculated
total_fire = 0 #the total amout of 


print("Cells:") #prints the cell part of the text
for cell in fire_cells:  # a loop to iterate trough all cells
    current_cell = cell.split(" = ") # a list ot store the split elements of the cell
    fire_type = current_cell[0] # a variable to take the type of the cell
    water_needed = int(current_cell[1]) # the amout of watter needed to put out the cell

    if current_water_amount < water_needed: # if the amount neeeded is bgger iy should put put the cell
        continue

    if current_water_amount <= 0:
        break
    
    #if the cell is one of the three types it's value should be prited, effrod calculated and total fire added 
    if (fire_type == "High" and  81 <= water_needed <= 125) or\
        (fire_type == "Medium" and  51 <= water_needed <= 80) or\
        (fire_type == "Low" and  1 <= water_needed <= 50):
        effort += water_needed * 0.25
        current_water_amount -= water_needed
        total_fire += water_needed
        print(f"- {water_needed}") #at the end print each cell in the correct format  



print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")






