def nacr_num(n):
    num = n
    list = []
    while n > 0:
        w = n % 10
        list.append(w)
        n = n // 10
    l = len(list)
    pow = [] 
    for i in range(l):
        pow.append(list[i]**l)
    narc = sum(pow)
    if narc == num:
        print("the number is narc")
    else:
        print("it ain't")
nacr_num(153)