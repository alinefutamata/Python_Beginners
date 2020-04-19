weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()

if unit == "L":
    your_weight = weight * 0.45
    print(f' You are {your_weight} Kilos')
elif unit == "K":
    your_weight = weight / 0.45
    print(f' You are {your_weight} Pounds')
else:
    print("Incorrect unit, please enter 'L' for Pounds and 'K' for Kilos")

