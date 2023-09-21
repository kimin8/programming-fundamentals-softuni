start = int(input())
end = int(input())
ans = ""

for i in range(start, end + 1):
    ans += f"{chr(i)} "
print(ans)