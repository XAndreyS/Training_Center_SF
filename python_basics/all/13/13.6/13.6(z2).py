#Задание 13.6.2
#Задание на самопроверку.

#Попробуйте теперь самостоятельно посчитать произведение всех чисел от 1 до N включительно.
#
#P =   # заводим переменную-счетчик, в которой мы будем считать произведение,
# подумайте чему она должна быть равна
#N = 5

# запишите цикл for для подсчета произведения

P = 1
N = 5

for i in range(1,N+1):
    print("Значение суммы на предыдущем шаге:",P)
    print("Текищее число", i)
    P *= i #тут я допустил ошибку написав P*=N
    print("Значение суммы после умножения:", P)
    print("---")
print("Конец цикла")
print("Ответ:сумма умножения=",P)
print()
print()
print("Ответ подсказка:")
"""обратите внимание, что P = 1, это важно, потому что если бы
мы умножали на 0, то все произведение было бы равно 0"""
P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
N = 5

# запишите цикл for для подсчета произведения
for i in range(1, N+1):
    print("ТЗ:",N)
    print("Ti:",i)
    P *= i
    print("TZ:",P)
    print("----")


print(P)
