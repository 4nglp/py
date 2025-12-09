t = [1,3,2,1,1]
rev = []
l = len(t)
while l >= 0:
    rev.append(t[l-1])
    l-=1

sym = True
for i in range(len(t)):
    if t[i] != rev[i]:
        sym = False 
print(sym)

s = True
b = len(t)
a = []
for i in range(b):
    a.append(t[b-1])
    if t[i] != a[i]:
        s = False
    b-=1
print(a)
print(s)
