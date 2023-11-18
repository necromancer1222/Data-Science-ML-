cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
        if len(name)<10:
                return name





short_cities=[]
'''
for city in cities:
        short_cities.append(is_short(city))
print(short_cities)


for city in cities:
        if is_short(city)!=None:
                short_cities.append(city)

 '''              
short_cities=[city for city in cities if is_short(city )!= None]
                
print(short_cities)


