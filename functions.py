def greet():
    print("Hello there!")
greet()

def greet(name):
    print("Hello", name)

greet("Haru")

def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 8

def greet(name="friend"):
    print("Hello", name)
greet()        # Hello friend
greet("Haru")  # Hello Haru

def introduce(name, age):
    print(f"My name is {name}, and I’m {age} years old.")
introduce(age=19, name="Haru")

def calc(a, b):
    return a + b, a * b, a - b
sum_, product, diff = calc(5, 3)
print(sum_, product, diff)
sum
#*args → for many positional arguments
def add_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total
print(add_all(1, 2, 3, 4))  # 10

count = 0
def increase():
    global count
    count += 1
increase()
print(count)  # 1

square = lambda x: x * x
print(square(5))  # 25
