fire_inputs = input().split("#")
water = int(input())

# high -> 81 - 125
# medium -> 51 - 80
# low -> 1 - 50

valid_cells = []
effort = 0
total_fire = 0

for sample in fire_inputs:
    fire_type, water_needed_string = sample.split(" = ")
    water_needed = int(water_needed_string)

    if water_needed <= water:
        if fire_type == "Low":
            if water_needed >= 1 and water_needed <= 50:
                water -= water_needed
                effort += (water_needed * 0.25)
                total_fire += water_needed
                valid_cells.append(water_needed)

        elif fire_type == "Medium":
            if water_needed >= 51 and water_needed <= 80:
                water -= water_needed
                effort += (water_needed * 0.25)
                total_fire += water_needed
                valid_cells.append(water_needed)

        elif fire_type == "High":
            if water_needed >= 81 and water_needed <= 125:
                water -= water_needed
                effort += (water_needed * 0.25)
                total_fire += water_needed
                valid_cells.append(water_needed)

# Output
print("Cells:")

for cell in valid_cells:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")