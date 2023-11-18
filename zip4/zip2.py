fn=["sherif","wael","loay"]
ln=["said","mohamed","kamal"]
gpa=[3.8,4,3.2]
print(list(zip(fn,ln,gpa)))


for i in zip(fn,ln,gpa):
    print(i)

x=list(zip(fn,ln,gpa))
for i in range(0,len(x)):
    print(x[i])

