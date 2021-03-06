'''
    a. выведите третий символ этой строки.
    b. выведите предпоследний символ этой строки.
    c. выведите первые пять символов этой строки.
    d. выведите всю строку, кроме последних двух символов.
    e. выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная
    с первого).
    f. выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
    g. выведите все символы в обратном порядке.
    h. выведите все символы строки через один в обратном порядке, начиная с последнего.
    i. выведите длину данной строки.
'''

stroka = 'How are you doing?'

print(stroka[2]) # третий символ этой строки
print(stroka[-2]) # предпоследний символ этой строки
print(stroka[:5]) # первые пять символов этой строки
print(stroka[:-2]) # вся строка, кроме последних двух символов
print(stroka[1::2]) # все символы с четными индексами
print(stroka[0::2]) # все символы с нечетными индексами
print(stroka[::-1]) # все символы в обратном порядке
print(stroka[::-2]) # все символы строки через один в обратном порядке
print(stroka[1:-1])
print(len(stroka)) # длина данной строки
