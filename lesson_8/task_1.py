orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Berry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berbd Klein', 3, 24.99]
]

for i in range(4):
    price = 0
    for j in range(4):
        price = orders[i][2] * orders[i][3]
        print(orders[i][j], end=' ')
        orders.append(price)
    print()
print(orders)







