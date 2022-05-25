prime_numbers = []

for num in range(2, 10):
    for x in range(2, num):
        if num % x == 0:
            break
    else:
        prime_numbers.append(num)

print(prime_numbers)

