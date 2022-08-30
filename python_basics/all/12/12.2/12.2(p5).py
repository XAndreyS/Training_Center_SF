#Строки
#объекты типа str — строки. Запись текстовых данных осуществляется с помощью апострофов и кавычек:
some_text = "python"
other_text = 'Java'
#если необходимо использовать апостроф или кавычки внутри самого текста:
introducing = "I'm Ivan"
action = 'Я читаю "Изучаем python" Марка Лутца'
#Использование одиночного апострофа внутри кавычек так же, как и кавычек внутри апострофов,
# не приведёт к появлению ошибки, в отличие от неправильной записи:
#introducing = 'I'm Ivan'
# SyntaxError: invalid character in identifier
long_text = '''Здесь может
               находиться
               большой "кусок" кода'''
other_long_text = """Таким образом тоже
                     можно записать"""
#Python позволяет получить доступ к отдельным символам или даже подстрокам,
# обращаясь к ним по индексам — порядковому номеру символа в строке:
s = "python"
print(s[0])
# p
print(s[1:4])
# yth
#строки являются неизменяемыми данными:
#s = "python"
#s[0] = 'C'
#print(s)
# ожидается вывод "Cython", однако python вернет ошибку:
# TypeError: 'str' object does not support item assignment
