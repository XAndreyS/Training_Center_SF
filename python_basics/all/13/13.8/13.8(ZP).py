
money_kid=0     #Стоимость билета для посетителей возрастом менее 18 лет
money_teen=990  #Стоимость билета для посетителей возрастом  от 18 лет до 24 лет
money_old=1390  #Стоимость билетов для посетителейвозрастом от 25 лет и старше
sum_money=[]    #Сумма стоимости билетов
sum_money_discount =()  #Сумма стоимости билетов со скидкой 10%
amount_visitor=()   #Количество посетителей
#далее ввод кол-ва посетителей и проверка на ввод только цифр и значени выше нуля
#Сначала запутался с добавлением "исключений" , подсмотрел у коллеги , что нуно "исключения" "засунуть" в
#цикл while
while True:
    try:
        amount_visitor=int(input('Введите количество посетителей:'))
    except ValueError as error:
        print("Не верный ввод!Вы должны вводить только  цифры:")
    else:
        if amount_visitor > 0:
            break
#Далее ввод возраста посетителей и проверка на ввод  только цифр и значений выше нуля
while True:
    try:
        age = [int(input("Введите возраст для посетителя(ей):")) for age_users in range(amount_visitor)]
    except ValueError as error:
        print("Не верный ввод!Вы должны вводить только  цифры:")
    else:
        break
print(f'Возраст посетителя(ей):{age}')
for j in age:
    age_money=j
    if age_money>=18 and age_money<25:
        sum_money.append(money_teen)
    elif age_money>=25:
        sum_money.append(money_old)
    elif age_money<18:
        sum_money.append(money_kid)
print(f'Стоимость билета{sum_money}')
sum_money=sum(sum_money)
print(f'Сумма стоимости билетов:{sum_money}')
if amount_visitor>3:
    sum_money_discount=round(sum_money-(sum_money * 0.1))
print(f'Сумма стоимости билетов с учётом скидки :{sum_money_discount}')