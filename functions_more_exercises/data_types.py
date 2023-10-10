datatype = input()
def get_value(a):
    if a == "int":
        return int(input()) * 2
    elif a == "real":
        return f"{float(input()) * 1.5:.2f}"
    elif a == "string":
        value = input()
        return f"${value}$"
    
print(get_value(datatype))