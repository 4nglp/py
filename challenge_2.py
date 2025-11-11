n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

num = abs(n)
rev = 0

while num > 0:
    digit = num % 10       
    print(digit)
    rev = rev * 10 + digit
    num //= 10

if n < 0:
    rev = -rev 

print("Reversed number:", rev)
