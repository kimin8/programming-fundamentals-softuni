initial_energy = 100
initial_coins = 100
collection_working_day_events = input().split("|")

for element in collection_working_day_events:
    name_or_ingredient, number = element.split("-")
    number = int(number)

    if name_or_ingredient == "rest":
        current_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif name_or_ingredient == "order":
        if initial_energy - 30 >= 0:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {name_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {name_or_ingredient}.")
            completed = False
            break
else:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")