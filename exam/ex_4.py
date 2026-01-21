def nchiff(x):
    occ = 0
    x = abs(x)
    while x > 0:
        x = x//10
        occ = occ + 1
    return occ
num = int(input("enter a num: "))
print(f'ur {num} has {nchiff(num)} digits')