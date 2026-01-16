def nchiff(x):
    occ = 0
    print(x)
    while x > 0:
        x = x//10
        occ += 1
    print(occ)
nchiff(1234)