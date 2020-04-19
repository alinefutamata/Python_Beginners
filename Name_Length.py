full_name = input("What's your full name? ")

if len(full_name) <3:
    print("Name mus be at least 3 characteres")

elif len(full_name) > 50:
    print("Name can be a maximum of 50 characteres")
else:
    print("Name looks good!")