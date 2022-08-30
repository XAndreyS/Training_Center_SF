

import time #добавил измерение времени работы, в основном для тестов, оставил как фичу
start_time = time.time()
while True: # Исключения. для ввода только целых чисел
    try:
        numbers = list(map(int,input("Введите последовательность чисел через пробел:").split())) # Сосдание списка из введенных пользователем чисел
        if len(numbers)==0: #Исклюение для пустого списка
            raise ValueError
    except ValueError as error:

        print("Не верный ввод!Вы должны вводить только  цифры,через пробел!")

    else:
        break

while True:# Исключения. для ввода только целых чисел
    try:
        number = int(input('Введите любое число:')) # Веедённое пользователем число
    except ValueError as error:
        print("Не верный ввод!Вы должны вводить только цифры,и только одно число")
    else:
        break

def merge_sort(array):  # для сортировки списка numbers используем алгоритм сортировки слиянием
    if len(array) < 2:
        return array[:]
    else:
        midle = len(array) // 2
        left = merge_sort(array[:midle])
        right = merge_sort(array[midle:])
        return merge(left,right)

def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def count(array, element): # Поиск повторяющихся чисел в списке numbers
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count


def binary_seearch(array, element, left, right): # для поискавведённого числа используем алгоритм бинарного поиска,
    if left > right or count_number >1: # добавил or count_number для поиска первого числа, если введены несколько повторяющихся чисел
                                        # при таком изменении в некоторых случчаях возникала ошибка RecursionError,для чего и добавил исключения
        element -=1  # если введёного пользовалелем числа нет всписке, ищем ближайшее
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_seearch(array, element, left, middle - 1)
    else:
        return binary_seearch(array, element, middle + 1, right)


def find(array, element): #при возникновении ошибки RecursionError, переходим на линейных алгоритм поиска
    for i, a in enumerate(array):
        if a == element:
            return i
    return False



count_number = count(numbers,number) #для удобства создат переменную для хранения кол-ва повторяющихся чисел в списке numbers
for_index_number = merge_sort(numbers) # Сохраняем в переменную работу функции сортировки списка numbers
min_index = for_index_number.index(min(for_index_number)) #Создаём переменную для хранения минимального индекса списка numbers
max_index = for_index_number.index(max(for_index_number)) #Создаём переменную для хранения минимального индекса списка numbers
"""Создание этих переменных(for_index_number,min_index,min_index) позволили мне сократить время работы программы
(особенно при работе сбольшим списком numbers) """
for_min_index = for_index_number[min_index]
for_max_index = for_index_number[max_index]
print()
print(f'Введённая последовательность чисел:{" ".join(map(str,numbers))}')
print(f'Введённое число:{number}')
print(f'Количество повторений введённого числа {number}:{count(numbers,number)} раз(а)')
print(f'Осортированная последовательность введённых чисел:{" ".join(map(str,for_index_number))}')


try: #Пока таким образом создаём исключение, если введенное больше\меньше максимального\минимального в списке последовательности чисел
    if for_min_index> number or number> for_max_index:
        raise ValueError ('Введёное число вне границ введённой последовательности чисел')
    elif for_min_index == number: #Исключение если введённое число первое в списке последовательности чисел
        raise ValueError ('Введённое число первое в списке последовательности чисел')

except ValueError as error:
    print(error)
    print("")
    exit()

if True:
    try:#Исключения для ошибки RecursionError
        if count_number == 1:   #если нет повторяющихся чисел запрашиваемых пользователем в списке numbers,
            print(f'Индекс предыдущего числа = {binary_seearch(for_index_number,number,min_index, max_index)-1}') # вызываем функцию бинарного поиска введённого пользователем числа и печатаем предыдущее(уменьшаем на 1)
        elif count_number > 1:  # если есть повторяющиеся числа запрашиваемого числа в списке numbers
            print(f'ИндекС предыдущего Числа = {binary_seearch(for_index_number, number, min_index, max_index) + 1}') #вызываем функцию бинарного поиска введённого пользователем числа и увеличиваем на 1(пока исправлял возможные ошибки, так получилось)
        else: # Если введёного пользователем числа нет в списке numbers                                                     #при различных комбинациях  с повторяющимися числами бывает ошибочный результат
            print(f'Индекс предыДущего ЧислA = {binary_seearch(for_index_number, number, min_index, max_index)}')  # вызываем функцию бинарного поиска , без уменьшения на 1,т.к. алгоритм поиска найдёт меньшее ближайшее меньшее число в списке
    except RecursionError as error: # если ошибка в функции бинарного поиска,
        print(f'Индекс предыдущего числA = {find(for_index_number, number) - 1}') #вызываем функцию линейного поиска введённого пользователем числа и печатаем предыдущее(уменьшаем на 1)


"""Возможно стоит добавить описание для подсчёта времени работы программы"""
"""Исключения по границам введённых чисел, подумать,как сделать код лаконичней?"""



print("--- %s seconds ---" % (time.time() - start_time))

#"Version 3.1 + anotacii 2.3"