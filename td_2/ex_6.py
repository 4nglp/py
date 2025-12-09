import math

t1 = [i for i in range(0,52,2)]
t2 = [math.cos(i**2) for i in t1 ]
print(min(t2))
print(t2.count(max(t2)))
