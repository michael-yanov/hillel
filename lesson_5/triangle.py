# rows = 7
# cols = 13

# for i in range(rows):
#     print(i, end='\t')
#     for j in range(cols):
#         if (i == rows - 1
#                 or i == 0 and j == cols // 2 or j == cols // 2 + i or j == cols // 2 - i):
#             print('* ', end='')
#         else:
#             print('  ', end='')
#     print()

# print('=' * 50)
#
# for i in range(rows):
#     #print(i, end='\t')
#         for j in range(cols):
#             if (i == rows - 1 or j == cols // 2 or j == cols // 2 + i or j == cols // 2 - i):
#                 print('* ', end='')
#             else:
#                 print('  ', end='')
#         print()

a = 7
for i in range(a):
    print(i, end='\t')
    for j in range((a - i)-1):
        print(end=" ")
    for j in range(i + 1):
        print("* ", end="")

    print()

print('/' * 50)

for i in range(a):
    print(i, end='\t')
    for j in range((a - i)-1):
        print(end=" ")
    for j in range(i + 1):
        if i == a - 1 or j == i:
            print("* ", end="")
    print()
