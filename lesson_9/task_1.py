'''
Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.
'''

def XOR_cipher(string, key):
    encrypt_string = []
    for i in string:
        encrypt_string.append(chr(ord(i) ^ key))
    return ''.join(encrypt_string)

string = str(input('Enter the string: '))
key = int(input('Enter the key: '))
print('encrypt string is: ', XOR_cipher(string, key))
encrypt_string = XOR_cipher(string, key)
print('original string is: ', XOR_cipher(encrypt_string, key))
