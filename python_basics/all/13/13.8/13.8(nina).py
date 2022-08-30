number_tickets=int(input("Введите количество билетов"))
total_price=0
for i in range(number_tickets):
    age=int(input("Введите возраст"))
    if age>=25:
        total_price=total_price+1390
    elif age<25 and age>=18:
        total_price = total_price + 990
    elif age<18:
        print("Бесплатный проход")
if number_tickets>3:
    total_price=total_price*0.9
print("Общая сумма:",total_price)
