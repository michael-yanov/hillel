string = 'AABABBAABBBAB'
string_new = []

for i in range(len(string)):
    if string[i] == 'A':
        string_new.append('B')
    else:
        string_new.append('A')
print(string)
print(''.join(string_new))