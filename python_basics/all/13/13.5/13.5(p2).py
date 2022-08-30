# Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

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