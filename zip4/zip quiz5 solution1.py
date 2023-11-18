cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i  in range(0,len(cast)):
    cast[i] = cast[i] + " " + str(heights[i])

print(cast)
