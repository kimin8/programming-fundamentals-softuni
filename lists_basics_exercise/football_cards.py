string_input = input()
commands = string_input.split(" ")

team_A = list(range(1, 12))
team_B = list(range(1, 12))

for command in commands:
    team, number = command.split("-")
    number = int(number)

    if team == "A" and number in team_A:
        team_A.remove(number)
    elif team == "B" and number in team_B:
        team_B.remove(number)

    if len(team_A) < 7 or len(team_B) < 7:
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if len(team_A) < 7 or len(team_B) < 7:
    print("Game was terminated")