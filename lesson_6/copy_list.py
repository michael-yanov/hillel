x = [1, 2, 3, 4, 5, 6, 7, 8]
y = x
print(x)
print(y)
x[3] = 100
print(x)
print(y)
print('*'*100)

_
y = x.copy()
print(x)
print(y)
x[6] = 200
print(x)
print(y)
print(id(x))
print(id(y))

