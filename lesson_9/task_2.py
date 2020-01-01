'''
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36)
'''

def convert_to(num, base):
    newNum = ''
    while num != 0:
        newNum = str(num % base) + newNum
        num = num // base
    return newNum


num = int(input('Enter the number: '))
base = int(input('Enter tne base: '))
print(convert_to(num, base))

