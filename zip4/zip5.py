fn=["sherif","wael","loay"]
ln=["said","mohamed","kamal"]
gpa=[3.8,4,3.2]
print(list(zip(fn,ln,gpa)))

d=zip(fn,ln,gpa)
print(d)

fn1,ln1,gpa1=zip(*d)
print(fn1)
print(ln1)
print(gpa1)

