# Exercise 1
# Write a program that generates a random number (0-10) and ask you to guess it. You have three asserts.
# - Define a random_number with randit between 0-10.
# - Initialize guesses_left to 3.
# - Use a while loop to let the user keep guessing so long as guesses_left is greater than zero.
# - Ask the user for their guess, just like the second example above.
# - If they guess correctly, print 'You win!' and break. Decrement guesses_left by one.
# - Use an else: case after your while loop to print:You lose.

import random

random_number = random.randint(0,10)
guess_left = 1

print("You have 3 asserts to guess the random number between 0 to 10. Good luck and let's get started! ")

while guess_left <= 3:
    number_guessed = int(input(f'Guess a number: '))
    guess_left += 1
    if random_number == number_guessed:
        print(f'Random number is: {random_number} ')
        print("You won!")
        break
else:
    print(f'Random number is: {random_number} ')
    print("You lost!")


