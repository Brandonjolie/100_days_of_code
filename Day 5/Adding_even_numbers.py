# even #s from 0 to 100
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num
print(total)
