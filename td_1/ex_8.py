number = int(input("Donnez un nombre positif : "))
digit = int(input("Donnez un chiffre (0-9) : "))
occ = 0
n = number
while n > 0:
    if n % 10 == digit:   
        occ += 1
    n = n // 10              
print("L'occurrence du chiffre", digit, "dans le nombre", number, "est", occ)
