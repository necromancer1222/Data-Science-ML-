basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
for fruit,no in basket_items.items():#('apples',4)
    print("fruit is {} and no is {}".format(fruit,no))

for fruit in basket_items.items():#('apples',4)
    print("fruit is {} and no is {}".format(*fruit))
