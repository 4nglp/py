n = int(input("enter a number to check if it is a perfect num or nah: "))
sum = 0
for i in range(1 , n):
    if n % i == 0:
        sum+=i
if sum == n:
    print("perfect")
else: 
    print("it ain't")