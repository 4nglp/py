n = int(input("Entrez un nombre : "))
if n < 2:
    print("Pas premier")
else:
    premier = True
    for i in range(2, n):
        if n % i == 0:
            premier = False
    if premier:
        print("Premier")
    else:
        print("Pas premier")
