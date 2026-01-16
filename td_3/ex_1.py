def power(a,b):
    if b == 0:
        return 1
    else:
        b = b-1
        return a**b * power(a,b)
print(power(2,3))

def fact(n):
    if n <= 1:
        return 1
    else: 
        return n * fact(n-1)
print(fact(3))

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

def pgcd(a,b):
    if b == 0:
        return a
    else:
        return pgcd(b,a%b)
print(pgcd(48,18))

def sum_list(list):
    if not list:
        return 0
    else:
        return list[0] + sum_list(list[1:])
print(sum_list([1,2,3]))

def sum_occ(list, n):
    if not list:
        return 0
    else:
        occ = 0
        if list[0] % 10 == n:
            occ = occ + 1
        return occ + sum_occ(list[1:], n)
print(sum_occ([1,2,2,2,4], 2))        

def sum_ch(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_ch(n//10)
print(sum_ch(1234))