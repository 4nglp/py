def inter(l,w):
    t=[]
    for x in l:
        if x in w and x not in t:
            t.append(x)
    return t
print(inter([1,2,3,4,5],[1,2,3,4,6]))

def comp(t):
    if not t:
        return []
    result = []
    max = t[-1]
    for x in range(max+1):
        if x not in t:
            result.append(x)
    return result
print(comp([0,1,5]))

def fus(l,w):
    f = []
    i,j = 0,0
    while i < len(l) and j < len(w):
        if l[i]<w[j]:
         f.append(l[i])
         i+=1
        elif w[j]<l[i]:
         f.append(w[j])
         j+=1
        else:
         f.append(l[i])
         i+=1
         j+=1
    f.extend(l[i:])
    f.extend(w[j:])
    return f
print(fus([3,6,8,26,109,133,165,181],[3,8,109,112,303]))    
