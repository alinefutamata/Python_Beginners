# Write a Python program that accepts a word from the user and reverse it

word = input("Please, write a word: ")
list_words = []

for item in word:
    list_words.insert(0, item)
print("".join(list_words))