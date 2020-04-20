total = 0
for interval in range(1,100):
    if interval % 3 == 0 or interval % 5 == 0:
        total += interval
print(total)