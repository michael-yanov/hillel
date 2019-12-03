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

all_students = first_class + second_class + third_class
desks_1_class = first_class //2 + first_class % 2
desks_2_class = second_class // 2 + second_class % 2
desks_3_class = third_class // 2 + third_class % 2
num = desks_1_class + desks_2_class + desks_3_class
print('Total number if students is {0}. You need to buy {1} desks.'.format(all_students, num))
