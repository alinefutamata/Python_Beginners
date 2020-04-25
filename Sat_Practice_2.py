# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius


temperature = float(input("What's today temperature? "))
type_temperature = input("Is it in Celsius (C) or Fahrenheit (F): ").upper()

if type_temperature == "C":
    fahrenheit = temperature * 1.8 + 32
    print(f"Your temperature is: {fahrenheit} in Fahrenheit.")
elif type_temperature == "F":
    celsius = (temperature - 32) / 1.8
    print(f"Your temperature is: {celsius} in Celsius.")
else:
    print("Please specify 'C' for Celsius and 'F' for Fahrenheit. ")
