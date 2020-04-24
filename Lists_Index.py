# Use the .index(item) function to find the index of "duck".
# Then .insert(index, item) the string "cobra" at that index.
# Print the result.

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print(animals.index("duck"))

animals.insert(1, "cobra")
print(animals)
