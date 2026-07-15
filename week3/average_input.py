total = 0
count = 0

# Repeatedly collect numbers until the user enters q
user_input = input("Enter a number or q to quit: ")

while user_input.lower() != "q":
    number = float(user_input)
    total += number
    count += 1

    user_input = input("Enter a number or q to quit: ")

if count > 0:
    average = total / count
    print("Numbers entered:", count)
    print("Total:", total)
    print("Average:", average)
else:
    print("No numbers were entered, so an average cannot be calculated.")