orders = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Berry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berbd Klein', 3, 24.99]
]

# orders_price = []
# orders_num = []
#
# orders_num = [i[0] for i in orders if len(i)] # first element from each list
#
#
# for i in range(len(orders)): # multiplication of price and quantity
#     price = 0
#     for j in range(len(orders)):
#         price = round(orders[i][2] * orders[i][3], 2)
#         if price < 100:
#             price += 10
#     orders_price.append(price)
# orders_new = tuple(orders_price)
#
# total_orders = list(map(lambda x, y: (x, y), orders_num, orders_price))
# print(total_orders)

total_orders = list(map(lambda x: (x[0], str(x[2]*x[3])), orders))
print(total_orders)







