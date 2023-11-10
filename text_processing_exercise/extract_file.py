elements = input().split("\\")
file_and_ext = elements[len(elements)-1]

file_name, file_extension = file_and_ext.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")