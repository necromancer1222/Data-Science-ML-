'''
squares=[]

for x in range(0,9):
    if x % 2 ==0:
        squares.append(x**2)
'''       


squares = [x**2 for x in range(0,9) if x % 2 == 0]
print(squares)
