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
#date[0] = date[0] + 1
# TypeError: 'tuple' object does not support item assignment
