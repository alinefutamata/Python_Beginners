# Write a Python program to construct the following pattern, using a nested for loop.


for x in range(6):
    stars = " *"
    for y in range(x):
        stars += "*"
    print(stars)

for x in range(6):
    stars = " *"
    for y in range(6-x):
        stars += "*"
    print(stars)