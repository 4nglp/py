L = int(input("L: "))
C = int(input("C: "))

while L <= 0 or L > 50 or C <= 0 or C > 50:
    print("1 ~ 50")
    L = int(input("L: "))
    C = int(input("C: "))

M = []
for i in range(L):
    line = []  
    for j in range(C):
        val = int(input(f"val of M[{i}][{j}]: "))
        line.append(val)
    M.append(line)

print("\nmat:")
for i in range(L):
    for j in range(C):
        print(f"{M[i][j]:5}", end=" ")
    print()

print("somme of ls")
for i in range(L):
    somme = 0  
    for j in range(C):
        somme += M[i][j]
    print(f"l {i+1} → {somme}")

print("somme of cs: ")
for j in range(C):
    somme = 0  
    for i in range(L):
        somme += M[i][j]
    print(f"c {j+1} → {somme}")