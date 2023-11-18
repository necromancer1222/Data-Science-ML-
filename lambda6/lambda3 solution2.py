cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]



is_short=lambda city: len(city) < 10

short_cities = list(filter(is_short, cities))


                
print(short_cities)
