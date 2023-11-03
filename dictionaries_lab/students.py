students = {}

user_input = input()

while ":" in user_input:
    parts = user_input.split(":")
    students[parts[1]] = {parts[0]: parts[2]}
    user_input = input()

for id, info in students.items():
    for key in info.keys():
        if info[key].split(" ") == user_input.split("_"):
            print(f"{key} - {id}")