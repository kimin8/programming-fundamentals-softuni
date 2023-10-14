happiness = list(map(int, input().split(" ")))
improvement = int(input())

after_improvement = [x * improvement for x in happiness]
employees = len(happiness)
average = sum(after_improvement) / employees
happy = list(filter(lambda x: x >= average, after_improvement))
sad = list(filter(lambda x: x < average, after_improvement))

if len(happy) >= employees / 2:
    print(f"Score: {len(happy)}/{employees}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{employees}. Employees are not happy!")