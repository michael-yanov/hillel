'''
Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на Bб а B, соответственно, на A.
В результате применения функции к исходной строке, функция должна вернуть строку: BBABAABBAAABA
'''

string = 'AABABBAABBBAB'
string_new = []

for i in range(len(string)):
    if string[i] == 'A':
        string_new.append('B')
    else:
        string_new.append('A')
print(string)
print(''.join(string_new))