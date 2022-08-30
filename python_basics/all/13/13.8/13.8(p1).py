#money_all =int()
#kol_vo= int(input("Введите кол-во билетов:"))
#
##for money in money_all:
#age=int(input("Введите возраст участника:"))
#if age>=18 and age< 25:
#    money = 990
#elif age>=25:
#    money=1390
#elif age<18:
#    money=0
#
#print("Сумма к оплате =",money)
n_c=int(input('Enter col-vo:'))
age = [int(input('Enter Age')) for i in range(n_c)]
print(age)
for j in age:
    print(j)
    if j >=18 and j <25:
        money=990
    elif j>=25:
        money=1390
    elif j<18:
        money=0
    print(money*age)

