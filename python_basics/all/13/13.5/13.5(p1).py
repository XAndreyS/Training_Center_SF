# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

#user_database = {
#    'iseedeadpeople': 'greedisgood',
#    'user': 'password',
#    'hesoyam': 'tgm'
#}
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