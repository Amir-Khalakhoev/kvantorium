estimates = []
print("Введите оценки ученика:")
for i in range(0, 10):
    estimates.append(int(input()))
sum_estimates = sum(estimates)
middle_value = sum_estimates / len(estimates)
print("Средний балл: ", middle_value)
