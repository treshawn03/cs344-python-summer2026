score = int(input("Enter your numeric score from 0 to 100: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a number from 0 to 100.")
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

if 0 <= score <= 100:
    print(f"Score: {score} -> Letter grade: {grade}") 