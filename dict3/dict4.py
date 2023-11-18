fruit_count=0
not_fruit_count = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#todo
for fruit, count in basket_items.items():
    if fruit in fruits:
       fruit_count =fruit_count + count
    else:
        not_fruit_count =not_fruit_count + count



print("The number of fruits is {} .There are {} items that are not fruits.".format(fruit_count, not_fruit_count))

#another way
fruit_count=0
not_fruit_count = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#todo
for key in basket_items.keys():
    if key in fruits:
       fruit_count =fruit_count + basket_items[key] 
    else:
        not_fruit_count =not_fruit_count + basket_items[key]



print("The number of fruits is {} .There are {} items that are not fruits.".format(fruit_count, not_fruit_count))

