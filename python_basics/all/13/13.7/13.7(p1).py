#Пример 3.
#
#Условие задачи. Дана двумерная матрица 3x3. Определите максимум и минимум каждой строки, а также их индексы.


random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

min_value_str =[]
max_value_str =[]
min_index_str =[]
max_index_str =[]

for i in random_matrix:
    min_index = 0
    max_index = 0
    min_value = i[min_index]
    max_value = i[max_index]
    for j in range(len(i)):
        if i[j]< min_value:
            min_value=i[j]
            min_index=j
        if i[j]> max_value:
            max_value=i[j]
            max_index=j
    min_value_str.append(min_value)
    min_index_str.append(min_index)
    max_value_str.append(max_value)
    max_index_str.append(max_index)
print(min_value_str)
print(min_index_str)
print(max_value_str)
print(max_index_str)



