salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", ...)

money_capital =
rest_of_money = money_capital + salary - spend

n = 10
m1 = 1

for m in range(2, n + 1):
    if rest_of_money + salary < spend:
        spend += spend * increase
        rest_of_money += salary - spend
        print(f"Траты за {m} месяц:", spend, )
        print(f"Остаток за {m} месяц:", rest_of_money)
        m1 += 1
        print(f"Число месяцев = {m1}")
