a = int(input('Enter the high of triangle: '))
for i in range(a):
    print(i, end='\t')
    for j in range((a - i)-1):
        print(end=" ")
    for j in range(i + 1):
        print("* ", end="")
    print()


