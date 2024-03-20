list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

# TODO найти сумму, количество и среднее арифметическое уникальных чисел
unique_numbers = set(list_)
sum_of_numbers = sum(unique_numbers)
count_of_numbers = len(unique_numbers)
сумма = sum(unique_numbers)
количество = len(unique_numbers)
average_of_numbers = round((сумма / количество), 5)

describe = {"Сумма уникальных чисел:" : сумма, "Количество уникальных чисел:" : количество,
            "Среднее арифметическое уникальных чисел:": average_of_numbers}
print(describe)