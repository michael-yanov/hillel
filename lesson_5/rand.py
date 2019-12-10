import random

lst = []
i = 0
while i < 100:
     lst.append(round(random.random() * 100, 2))
     lst.sort()
     i += 1
print(lst)

