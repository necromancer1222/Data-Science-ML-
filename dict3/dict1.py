basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
keys_items1=basket_items.keys()
print(keys_items1)
for i in keys_items1:
    print(i)
#print(keys_items1[0])


keys_items2=list(basket_items.keys())
print(keys_items2)
print(keys_items2[0])

val_items1=basket_items.values()
print(val_items1)
#print(val_items1[0])

val_items2=list(basket_items.values())
print(val_items2)
print(val_items2[0])

basket_items2=basket_items.items()
print(basket_items2)

#print(basket_items2[0])

basket_items2=list(basket_items.items())
print(basket_items2)
print(basket_items2[0])


