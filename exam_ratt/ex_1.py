def dig_occ(n,d):
    occ = 0
    while n > 0:
        w = n % 10
        if w == d:
            occ = occ + 1
        n = n // 10
    return occ
print(dig_occ(1223,2))