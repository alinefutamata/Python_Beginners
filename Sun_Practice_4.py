# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

list = []

for numbers in range(0,7):
    if numbers != 3 and numbers != 6:
        list.append(numbers)
        continue
print(str(list))