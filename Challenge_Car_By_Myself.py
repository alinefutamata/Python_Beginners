is_car_started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if is_car_started == True:
            print("Car already started")
        else:
            is_car_started = True
            print("Car is started... Ready to go!")
    elif command == "stop":
        if is_car_started == True:
            is_car_started = False
            print("Car stopped")
        else:
            print("Car already stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
