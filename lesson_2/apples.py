n = int(input('Enter number of students: '))
k = int(input('Enter number of apples: '))

apples = k // n
basket = k % n
print('Each student will take ', apples, 'apple(s) and ', basket, 'apple(s) in basket')