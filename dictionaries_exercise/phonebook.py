phonebook = {}

user_input = input()

while "-" in user_input:
    collection = user_input.split("-")
    phonebook[collection[0]] = collection[1]
    user_input = input()

user_input = int(user_input)

for i in range(user_input):
    search = input()
    if search in phonebook.keys():
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")