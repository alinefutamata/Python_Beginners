# print "Lucky Numbers! 3 numbers will be generated."
# "If one of them is a '5', you lose!"
import random

count = 0

print("""Lucky Numbers! 3 numbers will be generated
""")
while True:
    count += 1
    luck_numbers = random.randint(1, 6)
    if count == 3 and luck_numbers != 5:
        print(f'Lucky Numbers {count}: {luck_numbers}')
        print("You won!")
        break
    if luck_numbers == 5:
        print(f'Lucky Numbers {count}: {luck_numbers}')
        print("You lost!")
        break
    input(f'Lucky Numbers {count}: {luck_numbers}')






