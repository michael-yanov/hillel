s = 'hello, hohoho I am Santa, hohoho'

indexFirst = (s.find('h'))
indexLast  = (s.rfind('h'))

s_new = s[indexFirst + 1:indexLast]
print(s[indexFirst] + s_new.replace('h', 'H') + s[indexLast])
