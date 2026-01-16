def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)

def coef_binom(n,k):
        if k < 0 :
            return 0
        return fact(n)/(fact(k)*fact(n-k))

# nah