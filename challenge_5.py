import random

types = ["jbn", "gr3", "sif", "fls"]
nums = list(range(1, 13))

cards = []

for i in range(4): 
    t = random.choice(types)   
    n = random.choice(nums)  
    card = f"{t} {n}"
    cards.append(card)

print("Your 4 random cards:", cards)
