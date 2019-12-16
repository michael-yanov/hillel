# def print_some_text():
#     print('hello world')
#
#
# print_some_text()
#
# def multi():
#     print(3 * 8)
#
#
# multi(3, 5)


def my_print(*args, sep=' ', end='\n'):
    for element in args:
        print(element)


my_print(3, 6, 'g', True)

def func_2(**kwargs):
    print(type(kwargs))
    print(kwargs)


func_2(a=2, b=6, c=8)


def func_3(**kwargs):
    if 'a' in kwargs:
        print('parem A')
    if 'm' in kwargs:
        print('paarem m')
    if 'n' in kwargs:
        print('param n')


func_3(a=5, m=3, n=9)
