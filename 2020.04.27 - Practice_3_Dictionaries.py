# Reverse the Phone: 1234 into words: One Two Three Four

phone_number = input(f"What's your phone number: ")
written_number = []

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
for item in phone_number:
    word = numbers[item]
    written_number.append(word)
print(" ".join(written_number))