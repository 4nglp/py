import random

def gen_arr(vmin,vmax,smin,smax):
    size = random.randint(smin,smax)
    return [random.randint(vmin,vmax) for _ in range(size)]
arr0=[0,0,0,0]
arr1= gen_arr(0,41,3,6)
arr2= gen_arr(10,100,1,10)
print("arr1: ",arr1)
print("arr2: ",arr2)

def simple_fusion(lists):
    res = []
    for l in lists:
        res+=l
    return res
print("simple fusion")
print(simple_fusion([arr1,arr2]))

def sorted_fusion(lists):
    return sorted(simple_fusion(lists))
print("sorted")
print(sorted_fusion([arr1,arr2]))

def dib_fusion(lists):
    return list(set(simple_fusion(lists)))
print("dib")
print(dib_fusion([arr0,arr2]))

def alt_fusion(w,l):
    i,j=0,0
    res = []
    while i < len(w) or j < len(l):
        if i < len(w):
            res.append(w[i])
            i+=1
        if j < len(l):
            res.append(l[j])
            j+=1
    return res
print("alt")
print(alt_fusion([1,3,5],[2,4,6]))
 
def ord_fusion(l,w):
   i,j=0,0 
   res = []
   while i<len(l) and j<len(w):
    if l[i]<w[j]:
        res.append(l[i])
        i+=1 
    if w[j] < l[i]:
        res.append(w[j])
        j+=1
    return res + l[i:] + w[j:]
print("ord")
print(ord_fusion([1, 3, 4, 5], [2, 3, 6, 7, 8]))
        

