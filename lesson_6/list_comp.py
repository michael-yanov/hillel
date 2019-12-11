from random import randint
a = []
for _ in range(15): #в списке будут только четные элементы
    tmp = randint(1, 10)
    if not tmp % 2:
        a.append(tmp)
print(a)




b = [randint(1, 10) for _ in range(15)]
b = [x for x in b if not x % 2]
print(b)

x = [4, 8, 6, 10, 8]
y = ', '.join([str(el) for el in x])
print(y)

s = 'lower case string'
s = ''.join((ch.upper() if idx % 2 == 0 else ch for idx, ch in enumerate(s)))
print(s)