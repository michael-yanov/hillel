n = int(input('Enter number of students: '))
k = int(input('Enter number of apples: '))
if k >= n:
    apples = k // n
    basket = k % n
    print('Each student will take ', apples, 'apple(s) and ', basket, 'apple(s) will be in the basket')
else:
    print('You have no enough apples')