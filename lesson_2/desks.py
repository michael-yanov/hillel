'''
Desks and students
'''

first_class = int(input('Enter number of students in the first class: '))
second_class = int(input('Enter number of students in the second class: '))
third_class = int(input('Enter number of students in the third class: '))

# num = first_class + second_class + third_class
# desks = num // 2
#
# if (num % 2) == 0:
#     print('Total number of students  is', num,'.' ' You need to buy ', desks, 'desks for all classes')
# else:
#     desks += 1
#     print('Total number of students  is', num,'.' ' You need to buy ', desks, 'desks for all classes')

desks_1 = first_class // 2 + first_class % 2
desks_2 = second_class // 2 + second_class % 2
desks_3 = third_class // 2 + third_class % 2
all_classes = first_class + second_class + third_class
num = desks_1 + desks_2 + desks_3
print('Total number of students  is {0}. You need to buy {1} desks for all classes.'.format(all_classes, num))