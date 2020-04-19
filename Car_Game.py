command = input("> ").lower()
started = False

while command != "quit":
    if command == "start":
        if started == True:
            print("Car already started")
        else:
            print("Car started... Ready to go!")
            started = True
        command = input("> ").lower()
    elif command == "stop":
        if started == False:
            print("Car already stopped")
        else:
            print("Car stopped")
            started = False
        command = input("> ").lower()
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit = to exit""")
        command = input("> ").lower()
    elif command != "start" and "help" and "stop":
        print("I don't understand that...")
        command = input("> ").lower()
    else:
        break
