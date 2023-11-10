# aSd2&5s@1

text = input()
unique_chars = ""
current_symbol = ""
repetitions = ""

for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        unique_chars += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(unique_chars))}")
print(unique_chars)