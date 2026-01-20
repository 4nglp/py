def fact(n):
    if n <=1:
        return 1
    else:
        return n * fact(n-1)
    
def sum_arr(l):
    if not l:
        return 0
    else:
        return l[0] + sum_arr(l[1:])

def sum_num(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_num(n//10)

def occ_arr(l,n):
    if not l:
        return 0
    else:
        occ = 0
        if l[0] == n:
            occ = occ+1
        return occ + occ_arr(l[1:],n)