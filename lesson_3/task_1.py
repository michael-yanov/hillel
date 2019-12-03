'''
Square of integer numbers
'''

n = int(input('Enter the number: '))
i = 1
print(n, end='\t\t')
while (i ** 2) <= n:
    print(i ** 2, end='\t')
    i += 1