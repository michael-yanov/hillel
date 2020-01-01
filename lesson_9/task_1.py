def XOR_cipher(string, key):
    encrypt_string = []
    for i in string:
        encrypt_string.append(chr(ord(i) ^ key))
    return ''.join(encrypt_string)

string = 'hello guys'
key = 8
print('encrypt string is: ', XOR_cipher(string, 8))
encrypt_string = XOR_cipher(string, key)
print('original string is: ', XOR_cipher(encrypt_string, key))
