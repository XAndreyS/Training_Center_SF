#Список login_list хранит имена пользователей, а словарь password_list хранит имена (ключи) и пароли (значения).
#Задание 13.5.4

# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

#user_database = {
#    'user': 'password',
#    'iseedeadpeople': 'greedisgood',
#    'hesoyam': 'tgm'
#}
#
#def check_user(username, password):
#    ???
##Решение
login_list = [
   'root',
   'username1'
   ]

password_list = {
   'root': '1q2w3e4r',
   'username1': 'qwerty123'
}

username = input('Введите логин:\n')

if username in login_list:
   password = input('Введите пароль:\n')
   if password_list[username] == password:
       print('Вы успешно вошли в систему')
   else:
       print('Отказано в доступе')
else:
   print('Такого пользователя не существует')

#Моё решение

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

username = input("Enter user name:\n")
password = input("Enter your password:\n")
def check_user(username, password):
    if username in user_database.keys():
        if user_database[username] == password:

            return('You enter in system')
        else :
            return 'Bad paaasword'
    else :
        return 'not find your user name'

check = check_user(username, password)
print(check)