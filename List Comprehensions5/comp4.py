'''
squares=[]

for x in range(0,9):
    if x % 2 ==0:
        squares.append(x**2)
    else:
        squares.append(x+3)
'''

squares = [x**2 for x in range(0,9) if x % 2 == 0 else x+3]#err
print(squares)
