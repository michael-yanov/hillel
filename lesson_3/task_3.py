'''
Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
будет введён 0 (ноль), программа должна посчитать и вывести на экран:
- количество введённых чисел (завершающий 0 не считается)
- их сумму
- среднее арифметическое (не считая завершающего числа 0)
- определить максимальное и минимальное значение
- определить количество чётных и не чётных элементов в последовательности
'''

while True:
    n = int(input('Enter the number: '))
    if n == 0:
        break
