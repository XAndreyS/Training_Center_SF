"""Работа с вложенными циклами"""

"""
До этого мы обрабатывали списки и обходились для этого одним циклом, но что делать, 
если мы хотим обработать табличные значения?

matrix = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]

Такие таблицы ещё называют двумерными списками или двумерными матрицами. Двумерная матрица представляет собой обычную 
таблицу. Если одномерная матрица — это список, то двумерная — это список списков. Размер данной таблицы 3 х 2, 
три строки и два столбца.

Итак, для работы над матрицами нам нужны два цикла, где один вложен в другой. Для того, чтобы обойти всю таблицу,
 нужен цикл, который будет последовательно перебирать все строки, а также цикл, который будет перебирать все столбцы
  для каждой строки. То есть обход матрицы будет слева-направо, сверху-вниз.

Обычно индекс, который отвечает за строки обозначают как i, а индекс, отвечающий за столбцы — j, тогда:
"""
N = 2
M = 3
# заполнили матрицу последовательными числами
matrix = [
    [0, 1, 2],
    [3, 4, 5],
]


for i in range(N):  # цикл, отвечающий за строки
    for j in range(M):  # цикл, отвечающий за столбцы
        print(matrix[i][j], end=" ")
# 0 1 2 3 4 5
"""
Видим, что наша двумерная матрица распечатана в виде одномерной. Хотя все элементы последовательно расположены друг за
 другом. Чтобы она была распечатана в виде таблицы, нужно добавить print(), который будет выполняться после 
 обработки каждой строки:"""
for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()  # перенос на новую строку

# 0 1 2
# 3 4 5