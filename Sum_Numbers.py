limit_numbers = int(input("How many numbers do you want to sum? "))
counter = 0
soma_variavel = 0

while counter < limit_numbers:
    numbers = int(input("Numbers: "))
    soma_variavel += numbers
    counter += 1
print(f'Total: {soma_variavel}')






