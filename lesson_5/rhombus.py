# for rows in range(0, 7):
#     for cols in range(0, 7):
#         if rows + cols == 3 or cols - rows == 3 or rows - cols == 3 or rows + cols == 9:
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()
#
# print('/'*50)

n = int(input('Enter the high of rhombus: '))
for rows in range(1, n + 1):
    print(' ' * (n - rows) + '* ' * rows)
for rows in range (n - 1, 0, -1):
    # print(' ' * (n - rows) + '* ' * rows)
    if rows == n:
        print('* ', end=' ')
    else:
        print(end=' ')