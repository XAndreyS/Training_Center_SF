#Снова про неизменяемость
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
print()

#Задание 12.2.10 Какую ошибку покажет Python при выполнении кода?
#t = (0,1,2)
#t[1]  +=  1
#TypeError верно

