from getch import getch
from os import system

size = 4

CODE = 224
UP = 65
DOWN = 66
LEFT = 68
RIGHT = 67
ENTER = 13
SPACE = 32


def show(lst):
    system('clear')
    print('+----+----+----+----+')
    for i in range(size):
        for j in range(size):
            if '|{value:^4}'.format(value=lst[i][j] lst[i][j] == 16:
                print('', end=' ')
            else:
                print( lst[i][j], end=' ')
        print()


field = [j+1 + i*size for j in range(size) for i in range(size)]
x = 0
y = 0
field[y][x] = chr(42)
show(field)

while True:
    ch = ord(getch())
    if ch == SPACE:
        break
    elif ch == ENTER:
        print('x = {x}\ny = {y}'.format(x=x, y=y))
    elif ch == CODE:
        field[y][x] = '.'
        ch = ord(getch())
        if ch == UP:
            if y > 0:
                y -= 1
        elif ch == DOWN:
            if y < rows - 1:
                y += 1
        elif ch == LEFT:
            if x > 0:
                x -= 1
        elif ch == RIGHT:
            if x < cols - 1:
                x += 1
        field[y][x] = SYMBOL
        show(field)

