sequence = input().split(" ")
target = input()

palindromes = [word for word in sequence if word[::-1] == word]
print(palindromes)
print(f"Found palindrome {palindromes.count(target)} times")