# string = '1 2 3 4 5 6'
# new_string = string.split()
# a = []
# for i in new_string:
#     if i.isdigit():
#         a.append(float(i))
# print(sum(a) / len(a))

try:
    with open('students.txt', mode='r', encoding='utf-8') as input_file:
        lines = [line.split() for line in input_file]
        print(lines)

        # for i in lines:
        #     print(i)
            # for j in i:
            #     if j.isdigit():
except IOError as ex:
    print('Ooops, file not found.', ex)

