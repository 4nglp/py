for n in range(2, 101):
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
    if premier:
        print(n)
