def nacr_num(n):
    list = []
    while n > 0:
        w = n % 10
        list.append(w)
        n = n // 10
    l = len(list)
    pow = [] 
    for i in range(l):
        pow.append(list[i]**l)
    return sum(pow)
print(nacr_num(153))