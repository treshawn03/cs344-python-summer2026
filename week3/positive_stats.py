numbers = [12, -4, 7, 0, 15, -8, 22, 5, -1, 10]

positive_count = 0
positive_sum = 0

# Count and total the positive numbers
for number in numbers:
    if number > 0:
        positive_count += 1
        positive_sum += number

print("List:", numbers)
print("Positive numbers:", positive_count)
print("Sum of positive numbers:", positive_sum)
