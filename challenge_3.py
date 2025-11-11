n = int(input("enter a n: "))

if n > 50 or n <=0:
    print("it should be between 1 and 50 pls")
    n = int(input("enter a new n: "))

vals = []
for i in range(n):
    val = int(input(f'enter the value numner {i+1}: '))
    vals.append(val)

pos = 0
neg = 0
for v in vals:
    if v > 0:
        pos+=1
    if v < 0:
        neg+=1

print(f'pos: {pos}')
print(f'neg: {neg}')
