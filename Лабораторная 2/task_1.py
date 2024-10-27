money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
all_money = salary + money_capital
while all_money >= spend:
    all_money -= spend
    month += 1
    all_money += salary
    spend *= (increase + 1)


print("Количество месяцев, которое можно протянуть без долгов:", month)
