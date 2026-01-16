def ajouter_zeros_debut(L,n):
    for i in range(n):
        L.insert(0,0)
    print(L)
ajouter_zeros_debut([1,2,3],2)

def ajt_pols(p1,p2):
    if not p1:
        return p2
    if not p2:
        return p2
    return [p1[0] + p2[0]] + ajt_pols(p1[1:],p2[1:])
p1 = [1, 2, 3]
p2 = [2, 3, 4]
print(ajt_pols(p1, p2))

def evl_pol(p,x):
    if not p:
        return 0
    power = len(p) - 1
    return p[0]*(x**power) + evl_pol(p[1:],x)
print(evl_pol([4,2,3],2))
