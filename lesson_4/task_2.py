'''
Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения
задачи функцию `count`
'''

stroka = 'How are you doing bro?'
print('This sentenсe has {0} words'.format(stroka.count(' ') + 1))