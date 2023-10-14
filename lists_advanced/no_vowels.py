user_input = input()

no_vowels = [letter for letter in user_input if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(no_vowels))