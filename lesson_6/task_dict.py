'''
В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте.
'''
# s = 'just random text random print python pycharm python just python'
# s = s.split()
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# for i in d:
#     print(i, '-', d[i])
#
s = input('enter the string: ')
words = {}
for word in s.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print(words)

