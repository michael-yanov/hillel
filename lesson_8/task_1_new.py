orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Berry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berbd Klein', 3, 24.99]
]

total_orders = list(map(lambda x: (x[0], str('{0:.2f}'.format(x[2]*x[3] + 10)) if x[2]*x[3] < 100 else round(x[2]*x[3], 1)), orders))
print(total_orders)