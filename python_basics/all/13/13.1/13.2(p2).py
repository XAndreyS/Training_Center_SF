# Запишите вместо вопросительных знаков выражение, которое вернет True,
# если указывается високосный год, иначе False.
# Например, x = 2000 -> True; x = 1900 -> False; и т.д.
# Если есть сомнения в том, какие именно годы високосные,
# обратитесь к Википедии:
# https://ru.wikipedia.org/wiki/Високосный_год#Григорианский_календарь


x = int(input("Введиде год:"))
def is_leap_year(x):
    return (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))
x = (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))


print(x)
