text = input("Enter a line of text: ")
character = input("Enter a character to search for: ")

count = 0

# Count how many times the chosen character appears
for letter in text:
    if letter == character:
        count += 1

print("The character", character, "appears", count, "time(s).")