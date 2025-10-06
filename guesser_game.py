number=4
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    print("u have 3 tries and the number is between 1 and 10 gl!")
    guess = input("enter ur guess: ")
    guess = int(guess)
    if guess !=number:
        guess_count+=1
        print("wrong")
    elif guess ==number:
        print("WIIIIIIINNNNNNNNERRRRRR")
        break
print("game over")