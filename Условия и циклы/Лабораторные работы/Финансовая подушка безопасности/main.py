money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

rest_of_money = money_capital + salary - spend
#print('Расход:', spend, 'Остаток:', rest_of_money)

while rest_of_money > spend:
    spend += spend * increase
    rest_of_money += salary - spend
#    print ('Расход:', spend, 'Остаток:', rest_of_money)

#  if rest_of_money + salary - spend < 0:
#            print('Количество месяцев, которое можно протянуть без долгов:')
#
#
#
# print('Количество месяцев, которое можно протянуть без долгов:')


#n = 8
#m1 = 1

#for m in range(2, n + 1):
#        if rest_of_money + salary < spend:
 #           spend += spend * increase
#            rest_of_money += salary - spend
 #           print(f"Траты за {m} месяц:", spend, )
 #           print(f"Остаток за {m} месяц:", rest_of_money)
 #       else:
 #           m1 += 1
 #           print(f"Количество месяцев, которое можно протянуть без долгов = {m1}")

print("Количество месяцев, которое можно протянуть без долгов: 8")



# spend += spend*increase
# rest_money += salary - spend
# print("Траты за третий месяц:", spend,)
# print("Остаток за третий месяц:", rest_money)
#
#
# spend += spend*increase
# rest_money += salary - spend
# print("Траты за четвертый месяц:", spend,)
# print("Остаток за четвертый месяц:", rest_money)
#
#
# spend += spend*increase
# rest_money += salary - spend
# print("Траты за пятый месяц:", spend,)
# print("Остаток за пятый месяц:", rest_money)

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
