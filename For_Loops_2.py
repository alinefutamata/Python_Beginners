# Write a for loop that iterates over start_list = [5, 3, 1, 2, 4]
# and .append()s each number squared (x ** 2) to square_list(initialized to empty list).
# Then sort square_list.

start_list = [5, 3, 1, 2, 4]
square_list = []

for item in start_list:
    square_list.append(item ** 2)

square_list.sort()
print(square_list)
