n = int(input('Enter the high of triangle: '))
for rows in range(1, n + 1):
    for cols in range(1, 2 * n):
        if rows == n or rows + cols == n + 1 or cols - rows == n - 1:
            print('*', end='')
        else:
            print(end=' ')
    print()