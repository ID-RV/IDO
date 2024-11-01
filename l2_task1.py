money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

money_capital = money_capital + salary - spend
count_month = 1
while True:
    spend += spend * increase
    money_capital = money_capital + salary - spend
    if money_capital >= 0:
        count_month += 1
    else:
        break


print("Количество месяцев, которое можно протянуть без долгов:", count_month)
