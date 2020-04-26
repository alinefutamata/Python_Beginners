# Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = []
even_list = []

for item in numbers:
    if item % 2 == 0:
        odd_list.append(item)
    else:
        even_list.append(item)

print(len(even_list))
print(len(odd_list))

