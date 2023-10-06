progress = int(input())

bar = f"[{(progress//10)*'%'}{((10-(progress//10)))*'.'}]"

if progress < 100 and progress >= 0:
    print(f"{progress}% {bar}")
    print("Still loading...")
elif progress == 100:
    print("100% Complete!")
    print(f"{bar}")