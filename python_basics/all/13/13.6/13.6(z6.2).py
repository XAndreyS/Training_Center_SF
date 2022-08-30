
#N = 2
#M = 3
#matrix = [
#    [0, 1, 2],
#    [3, 4, 5],
#]
#
#for i in range(N):
#    for j in range(M):
#        print(matrix[i][j], end=" ")
#    print()  # перенос на новую строку
name = ['Lohmatiy', 'Lohmatiy', 'Шампунь', 'Кирантар','Шампунь', 'Маргнор', 'кито', 'Маки', 'Кишкоблуд']

species = ['Sapog', 'SS', 'Любимчик', 'Ворюга', 'Биб', 'мои', 'Её', 'сосед']
name_2 = ['Lohmatiy', 'Lohmatiy', 'Шампунь', 'Кирантар', 'Шампунь','Маргнор', 'кито', 'Маки', 'Кишкоблуд','Кирантар']
species_2 = ['Sapog',       'Sapog', 'Любимчик', 'Ворюга', 'Любимчик', 'мои',    'Её',  'сосед', 'Ворюга','Ворюга']
age_2 = ['1', '1', '11', '14', '11', '5', '1', '2','3', '14']
age = ['1', '11', '1', '14', '2', '5', '1', '2']
m = []
for i in zip(name_2, species_2, age_2):
    m.append(i)
matrix = []
for j in m:
    matrix.append(list(j))
print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)-i-1):
        if matrix[j] != matrix[j+1]:
            matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        else:
            print(f'Повторяющийся питомцец: {matrix[j]}')
print(matrix)





def set_matrix(list1, list2, list3):
    matrix = []
    for i in zip(list1, list2, list3):
        matrix.append(i)
    for j in matrix:
        matrix.append(list(j))
    for k in range(len(matrix)-1):
        matrix_set = matrix[k]
        if matrix_set != matrix[k+1]:
            return True




#N = len(matrix)
#M = 3
#for i in range(N):
    #for j in range(M):
        #matrix_set = {matrix[i][j]}
        #print(set(matrix[i][j]), end= " ")
        #print(matrix[i][j])
        #print(matrix_set)
    #print()  # перенос на новую строку