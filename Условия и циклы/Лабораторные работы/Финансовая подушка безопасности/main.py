money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

rest_money = money_capital + salary - spend
print("Остаток за первый месяц:", rest_money)

spend += spend*increase
rest_money += salary - spend
print("Траты за второй месяц:", spend,)
print("Остаток за второй месяц:", rest_money)

spend += spend*increase
rest_money += salary - spend
print("Траты за третий месяц:", spend,)
print("Остаток за третий месяц:", rest_money)


spend += spend*increase
rest_money += salary - spend
print("Траты за четвертый месяц:", spend,)
print("Остаток за четвертый месяц:", rest_money)


spend += spend*increase
rest_money += salary - spend
print("Траты за пятый месяц:", spend,)
print("Остаток за пятый месяц:", rest_money)

# while rest_money > 0:
#     rest_money = money_capital + salary - spend
#     print("Остаток за первый месяц:", rest_money)


# spend += (spend*increase)
# money_capital += salary
#
#
# a = money_capital + salary - spend
#
# (money_capital += salary - spend) > money_capital
# if (money_capital += salary - spend) > money_capital
#
# spend += (spend*increase)
# money_capital // ...
#
# print("Количество месяцев, которое можно протянуть без долгов:", money_capital // ...)
