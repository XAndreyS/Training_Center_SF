n_c=int(input('Enter kol-vo:'))
age=[]
money_kid=0
money_teen=990
money_old=1390
all_money=[]
all_money_s=()
s=n_c
for i in range(n_c):
    i=int(input('Enter age:'))
    age.append(i)
    print(age)
for j in age:
    age_money=j
    if age_money>=18 and age_money<25:
        all_money.append(money_teen)
    elif age_money>=25:
        all_money.append(money_old)
    elif age_money<18:
        all_money.append(money_kid)
print(all_money)
all_money=sum(all_money)
print(all_money)
if s>3:
    all_money_s=round(all_money-(all_money*0.1))
print(all_money_s)



