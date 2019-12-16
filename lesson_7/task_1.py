'''
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
(первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
'''


def arithmetic(a, b, operation):
    c = 0
    if operation == '+':
        c = a + b
    elif operation == '-':
        c = a - b
    elif operation == '*':
        c = a * b
    elif operation == '/':
        c = a / b
    else:
        print('Unknown operation')
    return c


x = arithmetic(10, 5, '*')
print(x)
