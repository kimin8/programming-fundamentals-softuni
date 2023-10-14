notes = [0] * 10
user_input = input()

while user_input != "End":

    tokens = user_input.split("-")
    priority = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(priority)
    notes.insert(priority, note)

    user_input = input()

result = [element for element in notes if element != 0]
print(result)