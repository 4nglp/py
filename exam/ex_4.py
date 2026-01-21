def nchiff(x):
    occ = 0
    x = abs(x)
    while x > 0:
        x = x//10
        occ = occ + 1
    print(occ)
nchiff(-12411)