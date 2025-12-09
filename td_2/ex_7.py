t = [1,1,2,1,1]
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