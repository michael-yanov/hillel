'''
Square of integer numbers
'''

n = int(input('Enter the number: '))
i = 1
while (i ** 2) <= n:
    print(n,'{:1d}'.format(i ** 2), end='')
    i += 1