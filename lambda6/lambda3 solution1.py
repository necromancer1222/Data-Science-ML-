cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):

    return len(name)<10

short_cities=list(filter(is_short,cities))
print(short_cities)
