#Целые числа
#Объекты типа int
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
# В результате получаются также целые числа (кроме операции деления, на которой мы остановимся чуть позже):
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