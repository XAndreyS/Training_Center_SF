#12.3. Типы данных: число, число с плавающей точкой
#Целые числа
a = 5/2
print(a)
# 2.5
print(1 // 3)
# 0
print(3 // 3)
# 1
print(29 // 3)
# 9

#об остатке от деления,
print(1 % 3) # ближайшее число, которое нацело делится на 3 - это ноль
# 1
print(3 % 3) # в этом примере сам делитель может нацело разделиться
# 0
print(29 % 3) # здесь ближайшее число - 27, и поэтому результат 29-27=2
# 2

#Давайте посмотрим на это правило на примере. В случае положительных чисел:
a = 5
b = 2
q = a // b # q = 2
r = a % b  # r = 1
#Посмотрим на несколько другую ситуацию:
a = -5
b = 2
q = a // b # хочется получить 2, как и в прошлый раз, но q = -3
r = a % b # а остаток остался тот же r = 1

#Задание 12.3.1
#Что получится в результате вычислений?
print ((31 % 2) + (-31 % 2))
#2

print (13 % -3 * 3 - 3**2)
#-15

#Длинная арифметика
f = 653457
g = 123493
print(f**g)
# 393354..282257

#Числа с плавающей точкой Десятичная форма
a = 5.4321
print(a)
# 5.4321
#экспоненциальная форма записи числа:
print(a**100)
# 3.138886636534116e+73

a = 5.4321**100 # 3.138886636534116e+73

print(a*100) # мантисса осталась прежней, а степень увеличилась на 2
# 3.138886636534116e+75

print(a*1000) # аналогично, только степень увеличилась уже на 3
# 3.138886636534116e+76

print(a/100) # снова мантисса не меняется, а степень уже уменьшилась
# 3.138886636534116e+71

print(a/1000) # как, наверное, уже ожидаемо, степень снова уменьшилась
# 3.138886636534116e+70
# 3.138886636534116e+73 - изначально
# 313.8886636534116e+73 - при умножении на 100
# 3138.886636534116e+73 - при умножении на 1000
# 0.03138886636534116e+73 - при делении на 100
# 0.003138886636534116e+73 - при делении на 1000

#Рассмотрим такой пример:
print(1/3)
# 0.3333333333333333
print(1.3+2.3)
# 3.5999999999999996

#Преобразование типов
#int для целых чисел,
#float для чисел с плавающей точкой.
print(3/2)
# 1.5
print(3.14*2)
# 6.28
print(float(1))
# 1.0
print(int(3.14))
# 3
print(int(2.8)) # ожидается 3, т.к. 2.8>2.5
# 2

#для корректного округления чисел с плавающей точкой по всем правилам необходимо пользоваться функцией round():
print(round(1.00+0.01-3.01))
# -2
print(3.14/2)
# 1.57
print(round(3.14/2, 1)) # второй аргумент - желаемое количество знаков
# 1.6