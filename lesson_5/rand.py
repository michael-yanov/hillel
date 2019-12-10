import random

down = int(input('Enter down border: '))
up = int(input('Enter up border: '))
indx = int(input('Enter type of value: 1 - integer, 2 - float: '))
while True:
    if indx == 1:
        print(random.randint(down, up))
    else:
        print(round(random.random() * (up - down) + down, 2))