s = 'Lorem Ipsum Lorem Ipsum Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.'
s = s.split()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
max_word = max(d.values())
for key, value in d.items():
    if value == max_word:
        print('The most used word is: ', key, '-', value)
