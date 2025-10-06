fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hi", 12, 3.5, True]
empty = []

fruits[0]       # 'apple' (first element)
fruits[-1]      # 'cherry' (last element)
fruits[1:3]     # ['banana', 'cherry'] (slice)
fruits[:2]      # ['apple', 'banana'] (first 2)
fruits[::2]     # ['apple', 'cherry'] (step of 2)

fruits.append("orange")       # add to the end
fruits.insert(1, "kiwi")      # insert at index 1
fruits.extend(["melon", "pear"])  # add multiple
fruits.remove("banana")  # remove by value
fruits.pop(2)            # remove by index (returns removed item)
fruits.pop()             # remove last item
del fruits[0]            # delete by indefruits = ["apple", "banana", "cherry"]
fruits.clear()           # remove everything

"apple" in fruits      # True
"mango" not in fruits  # True
index = fruits.index("banana")  # 1
count = fruits.count("apple")   # how many times "apple" appears


numbers = [5, 2, 8, 1]
numbers.sort()          # [1, 2, 5, 8]
numbers.sort(reverse=True)  # [8, 5, 2, 1]
fruits = ["banana", "apple", "cherry"]
sorted_list = sorted(fruits)  # creates new sorted list
fruits.reverse()         # reverse order (not sort)

a = [1, 2, 3]
b = a.copy()             # shallow copy
c = list(a)              # same as copy()

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

for i, fruit in enumerate(fruits):
    print(i, fruit)

a = [1, 2, 3]
b = [4, 5, 6]
merged = a + b           # [1, 2, 3, 4, 5, 6]

text = ["I", "love", "Python"]
sentence = " ".join(text)    # "I love Python"


