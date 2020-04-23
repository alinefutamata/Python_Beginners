numbers = [5, 2, 5, 2, 2]

for letter in numbers:
    letter_f = letter * "x"
    print(letter_f)

for x_count in numbers:
    output = " "
    for count in range(x_count):
        output += "x"
    print(output)