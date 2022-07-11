numbers = []
for i in range(0, 10):
    numbers.append(int(input()))
min_number = numbers[0]

for i in range(0, len(numbers)):
    if numbers[i] < min_number:
        min_number = numbers[i]

print()
print(min_number)
