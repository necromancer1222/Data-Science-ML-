x=["tamer","wael","sherif","wael","ahmed","mohamed","sherif"]
names=dict()#names={"tamer":1,"wael":2,"sherif":2,"ahmed":1,"mohamed":1}
for name in x:#name="ahmed"
    names[name]=names.get(name,0)+1#names["ahmed"]=names.get("ahmed",0)+1
print(names)
    
