s = 'just random text random print python pycharm python just python'
s = s.split()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(i, '-', d[i])
