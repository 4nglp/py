help_msg = '''
start - to start the car
stop - to stop the car 
quit - to exit
'''

while True:
    cmd = input(">").lower()
    if cmd == "start":
        print("3n3n3nnnnnnnnnn")
    elif cmd == "stop":
        print("nini")
    elif cmd == "help":
        print(help_msg)
    elif cmd == "quit":
        break
    else:
        print("me do not understand")
