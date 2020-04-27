# Write a program to remove the duplicates in a list

list = [1, 2, 3, 4, 4, 5, 20, 54, 2, 4]
numbers = []

for item in list:
    if item not in numbers:
        numbers.append(item)
print(numbers)