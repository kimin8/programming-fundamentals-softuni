number = int(input())
proper_divisors = []

for i in range(1, number):
    if number % i == 0:
        proper_divisors.append(i)

sum_of_divisors = sum(proper_divisors)

if number == sum_of_divisors:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")