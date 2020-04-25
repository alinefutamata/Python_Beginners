# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the
# prompt appears again until the guess is correct, on successful guess, user will
# get a "Well guessed!" message, and the program will exit.

secret_number = 6

print("Let's get started! Guess a number between 1 to 9. ")
while True:
    guess_number = int(input("Guess a number: "))
    if guess_number == secret_number:
        print("Well Guessed! ")
        break
    else:
         print("Try again! ")