a = set()
print(a)
a = set('hello')
print(a)
a = {'a', 'b', 'c', 'd'}
print(a)
a = {i ** 2 for i in range(10)} # генератор множеств
print(a)
a = {}  # А так нельзя!
type(a)

print(a)