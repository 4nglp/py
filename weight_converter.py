weight = input("enter it: ")
type = input("k or l: ")
if type.upper() == "K":
    weight =float(weight) * 2.2 
    print(f'ur {weight} pounds')
elif type.upper() =="L":
    weight = float(weight) / 2.2 
    print(f'ur {weight} kgs')
else:
    print("l or k there's no other weight option lol")