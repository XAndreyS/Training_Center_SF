#12.2. Неизменяемые типы данных
#Возможности языка Python позволяют узнавать тип переменной, используя встроенную функцию type():
a = 3.14
b = '3.14'

print(type(a))
# <class 'float'>
print(type(b))
# <class 'str'>

#Целые числа Объекты типа int
a = 1
b = 73
c = -12
d = 2
#С помощью функции type() можем удостовериться, что мы создали переменные, в которых хранится целочисленный объект:
print(type(a))
# <class 'int'>
print(type(b))
# <class 'int'>
print(type(c))
# <class 'int'>
print(type(d))
# <class 'int'>
#С такими объектами можно производить известные операции: сложение, вычитание, умножение и возведение в степень.
e = a+b
print(e)
print(type(e))
# 74
# <class 'int'>

f = b*c
print(f)
print(type(f))
# -876
# <class 'int'>

g = b**d # оператор возведения в степень в python обозначается как **
print(g)
print(type(g))
# 5329
# <class 'int'>

#Числа с плавающей точкой  подразумеваются дробные числа
x = 0.1
y = 21.5

print(type(x))
# <class 'float'>
print(type(y))
# <class 'float'>

#С числами с плавающей точкой можно производить уже все знакомые операции, в том числе и деление:
z = y / x
print(z)
print(type(z))
# 215.0
# <class 'float'>

#Задание 12.2.4
print (0.1+0.1*5-0.3*4)
#-0.6
#Задание 12.2.5
print ((3.14+0.3)/2+0.15)
#1.87

#Обмен значениями
#Подумайте самостоятельно, как совершить обмен значениями численных переменных, используя только действия
# сложения и вычитания.
a = a - b
b = a + b
a = b - a

#Задание 12.2.7
a = -13
b = 7
#-20

#Строки используются объекты типа str — строки.
some_text = "python"
other_text = 'Java'
introducing = "I'm Ivan"
action = 'Я читаю "Изучаем python" Марка Лутца'
long_text = '''Здесь может
               находиться
               большой "кусок" кода'''
other_long_text = """Таким образом тоже
                     можно записать"""

#Python позволяет получить доступ к отдельным символам или даже подстрокам,
# обращаясь к ним по индексам — порядковому номеру символа в строке:
s = "python"
print(s[0])
# p
print(s[1:4])
# yth
#Несмотря на то, что мы можем прочитать отдельный символ, перезаписать мы его не можем,
# потому что строки являются неизменяемыми данными:
s = "python"
s[0] = 'C'
print(s)
# ожидается вывод "Cython", однако python вернет ошибку:
# TypeError: 'str' object does not support item assignment

#Логические переменные
t = True
f = False
#гические значения можно получать и как возвращаемое значение некоторых действий, таких как сравнение:
print(3 > 10)
# False

print(3 < 10)
# True

print(3 == 10) # равны ли объекты?
# False
#
#Можно также проверить, содержится ли какой-то символ в строке:
print('r' in 'world') # проверяем отдельный символ
# True

print('th' in 'python') # проверяем целую подстроку
# True

print('the' in 'python')
# False

#Задание 12.2.9
1.57*3/1.5 == 3.14

#True верно
'PY' in "Python"

#False

#Кортеж
#Для сохранения нескольких объектов (необязательно текстовых) в одну переменную можно использовать кортежи (tuple).
# Чтобы создать кортеж, нужно записать данные в круглые скобки через запятую:
date = (1, 'january', 2020)
#После чего можно получить доступ к отдельным переменным по индексу:
print(date[0])
# 1
print(date[1])
# january
print(date[2])
# 2020
#В связи с тем, что кортеж, так же как и другие приведённые выше типы, является неизменяемым,
# попытка его модифицировать приведёт к ошибке:
date[0] = date[0] + 1
# TypeError: 'tuple' object does not support item assignment

#Снова про неизменяемость
#Когда мы кратко познакомились с основными неизменяемыми типами данных, ещё раз посмотрим,
# как проявляется это свойство на примере строк.
#Пусть у нас будет две строки:
s1 = "foo"
s2 = "bar"
#Допишем вторую строку к первой:
s1 = s1+s2
print(s1)
# foobar

s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 139953609727144, foo

s2 = "bar"
print(id(s2), s2) #проверяем идентификатор
# 139953609727088, bar

s1 = s1+s2
print(id(s1), s1) #проверяем идентификатор
# 139953459591296, foobar

#Задание 12.2.10
t = (0,1,2)
t[1]  +=  1
#TypeError верно 