#Получилось 2 варианта, не смог выбрать более подходящий и  решил оставить оба
print("Вариант1:")

per_cent = {'ТКБ':5.6,'СКБ':5.9,'ВТБ':4.28,'СБЕР':4.0}
money = int(input("Введите сумму:"))

deposit = [ money * (per_cent.get('ТКБ')/100),money * (per_cent.get('СКБ')/100),money * (per_cent.get('ВТБ')/100),
            money * (per_cent.get('СБЕР')/100)]
deposit = list(map(round,deposit))
deposit_i = max(deposit)

print ('Накопления за год:"ТКБ","СКБ","ВТБ","СБЕР"')
print(deposit)
print ("Максимальная сумма, которую вы можете заработать:","\n", deposit_i)#сначала не много затупил и не мог "засунуть" в одну команду строку и данные подсчёта,ошибка была в неправильных скобках
#print ("Максимальная сумма, которую вы можете заработать:")
#print(deposit_i)

print ("Вариант2:")
per_cent = {'ТКБ':5.6,'СКБ':5.9,'ВТБ':4.28,'СБЕР':4.0}
money = int(input("Введите сумму:"))
TKB = money * (per_cent.get('ТКБ')/100)
SKB = money * (per_cent.get('СКБ')/100)
VTB = money * (per_cent.get('ВТБ')/100)
SBER = money * (per_cent.get('СБЕР')/100)
#deposit = [round(TKB),round(SKB),round(VTB),round(SBER)]
deposit = list(map(round,deposit)) #долго мучился с округлением в списке, пока не вспомнил про map
deposit_i = max(deposit)

print ('Накопления за год:"ТКБ","СКБ","ВТБ","СБЕР"','\n',deposit)
print()
print ("Максимальная сумма, которую вы можете заработать:",deposit_i)
