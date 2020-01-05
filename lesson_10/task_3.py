d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}
d1 = {}
for key, value in d.items():
    d1[value[1]] = key
print(d1)
