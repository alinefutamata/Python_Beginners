# Reverse the Phone: 1234 into words: One Two Three Four

phone_number = input(f"What's your phone number: ")
written_number = []

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
}
for item in phone_number:
    word = numbers.get(item, "Item not found")
    written_number.append(word)
print(" ".join(written_number))