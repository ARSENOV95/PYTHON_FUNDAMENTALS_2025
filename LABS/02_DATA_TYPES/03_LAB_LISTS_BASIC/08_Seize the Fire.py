fire_cells = input().split("#")
current_water_amount = int(input())

effort = 0 
total_fire = 0


print("Cells:")
for cell in fire_cells:
    current_cell = cell.split(" = ")
    fire_type = current_cell[0]
    water_needed = int(current_cell[1])

    if current_water_amount < water_needed:
        continue

    if (fire_type == "High" and  81 <= water_needed <= 125) or \
        (fire_type == "Medium" and  51 <= water_needed <= 80) or \
        (fire_type == "Low" and  1 <= water_needed <= 50):
        effort += water_needed * 0.25
        current_water_amount -= water_needed
        total_fire += water_needed
        print(f"- {water_needed}")




    
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")






