import random

t = []          
for i in range(3):
    layer = []
    for j in range(3):
        row = [] 
        for k in range(3):
            row.append(random.randint(0,1)) # can use random() for vals between 0 and 1
        layer.append(row)
    t.append(layer)
print(t)
print("1st element  :", t[0][0][0])
