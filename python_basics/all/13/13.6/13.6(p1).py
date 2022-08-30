#Пример 1.
#
#Условие задачи. Найдите сумму всех натуральных чисел от 1 до N включительно.
#
#Для начала нам нужно завести переменную, куда мы будем с вами суммировать все числа, пусть это будет переменная S.
# Где нам взять последовательность чисел от 1 до N включительно? Для этого есть функция range(),
# которая как раз сделает последовательность нужных нам чисел. Функция range может работать тремя способами:
#1)range(END);
#2)range(START, END);
#3)range(START, END, STEP).


S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
    print("Значение суммы на предыдущем шаге: ", S)
    print("Текущее число: ", i)
    S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
    print("Значение суммы после сложения: ", S)
    print("---")
print("Конец цикла")
print()
print("Ответ: сумма равна = ", S)