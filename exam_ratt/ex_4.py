def power(k):
    if k%2 == 0:
        return 1
    if k%2 != 0:
        return -1

# 2 time and space complexity yet to be revised

def term(k):
    if k <= 0:
        return 0
    else: 
        return (4*((-1)**k+1))/(2*k*(2*k+1)*(2*k+2))

def term_arr(n):
    if n <= 0:
        return 0
    else:
        arr = []
        while n > 0:
            arr.append(term(n))
            n = n - 1
        return arr

def sum_arr(l):
    if not l:
        return 0
    else:
        return l[0]+sum_arr(l[1:])

def pi(n):
    if n <= 0:
        return 0
    else:
       return 3 + sum(term_arr(n)) 
print(pi(3))
