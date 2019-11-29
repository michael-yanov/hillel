'''
Desks and students
'''

first_class = int(input('Enter number of students in the first class: '))
second_class = int(input('Enter number of students in the second class: '))
third_class = int(input('Enter number of students in the third class: '))

num = first_class + second_class + third_class
desks = num // 2

if (num % 2) == 0:
    print('Total number of students  is', num,'.' ' You need to buy ', desks, 'desks.')
else:
    desks += 1
    print('Total number of students  is', num,'.' ' You need to buy ', desks, 'desks for all classes')
