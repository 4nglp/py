L = [8, 3, 15, 4, 1, 9, 20, 7]
print("original :", L)
L.sort()
print("sorted: ", L)
cities = ["Rabat", "casablanca", "Fes", "Berkane", "Taza"]
print("original: ", cities)
sorted_cities = sorted(cities) # may add reverse =  True
print("sorted: ", sorted_cities)
# ascii order the Ms are always before the ms can use key = str.lower