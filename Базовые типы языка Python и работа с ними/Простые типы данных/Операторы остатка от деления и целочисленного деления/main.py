HOURS_IN_DAY = 24  # количество часов в дне постоянно
total_hours = 5000  # дано по задаче

days = ...  # TODO найти полное количество дней
hours = ...  # TODO найти оставшееся количество часов

days = total_hours // HOURS_IN_DAY
hours = total_hours % HOURS_IN_DAY

print("Количество дней =", days)
print("Оставшееся количество часов =", hours)


