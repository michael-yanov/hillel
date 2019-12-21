orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Berry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berbd Klein', 3, 24.99]
]

orders_price = []
orders_num = []

orders_num = [i[0] for i in orders if len(i)]


for i in range(len(orders)):
    price = 0
    for j in range(len(orders)):
        price = int(orders[i][2] * orders[i][3])
        if price < 100:
            price += 10
    orders_price.append(price)
    #print()
orders_new = tuple(orders_price)

print(orders_num)
print(orders_price)

total_orders = list(map(lambda x,y: (x,y), orders_num, orders_price))
print(total_orders, sep='\n')








