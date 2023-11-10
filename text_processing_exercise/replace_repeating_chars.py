text = input()
final_answer = ""
last_added_character = ""
for char in text:
    if char != last_added_character:
        final_answer += char
    last_added_character = char

print(final_answer)