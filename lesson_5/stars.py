rows = 7
cols = 13

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == rows - 1
                or j == cols // 2 and i == 0 or j == cols // 2 + i or j == cols // 2 - i):
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print('=' * 40)

for i in range(rows):
    print(i, end='\t')
    for j in range(cols):
        if (i == rows - 1
                or j == cols // 2 or j == cols // 2 + i or j == cols // 2 - i):
            print('* ', end='')
        else:
            print('  ', end='')
    print()

print()