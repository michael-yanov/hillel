'''
Square of integer numbers
'''

n = int(input('Enter the number: '))
i = 1
while (i ** 2) <= n:
    #print(i ** 2)
    print('{0} {1}'.format(n, i ** 2), end = ' ')
    i += 1