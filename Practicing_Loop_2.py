# Create a for loop that prompts the user for a hobby 3 times, then appends each one to hobbies.

hobbies = []
count = [1, 2, 3]

for hobby in count:
    list_hobbies = input(f"Tell me your hobby number {hobby}: ")
    hobbies.append(list_hobbies)

print(f'My three hobbies are: {hobbies[0]}, {hobbies[1]} and {hobbies[2]}')
