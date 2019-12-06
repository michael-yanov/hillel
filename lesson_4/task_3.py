'''
Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов `ch`.
Для решения можно использовать только функцию `find`(rfind), операторы  `if` и `for`(while).
'''

s = input('Enter the string: ')
ch = input('Enter symbol for searching: ')
l = 0
for i in range(len(s)):
    if s[i] == ch:
        l += 1
print('Found {0} symbols'.format(l))