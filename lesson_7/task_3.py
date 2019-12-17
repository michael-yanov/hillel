'''
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
'''

def square(a):
    per = a * 4
    sq = a ** 2
    diag = pow(2, 0.5) * a
    return per, sq, diag

perSq, sqSq, diagSq = square(20)
print('Perimeter: {0}\nSquare: {1}\nDiagonal: {2}'.format(perSq, sqSq, round(diagSq, 2)))