# Planned Functions
# 1. get_score() - Gets and validates the user's score.
# 2. calculate_grade() - Determines the letter grade.
# 3. display_results() - Displays the score and letter grade.


def get_score():
    """Prompt the user for a score."""
    return int(input("Enter your numeric score from 0 to 100: "))


def calculate_grade(score):
    """Return the correct letter grade."""

    if score < 0 or score > 100:
        return None
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def display_results(score, grade):
    """Display the results."""

    if grade is None:
        print("Invalid score. Please enter a number from 0 to 100.")
    else:
        print(f"Score: {score} -> Letter grade: {grade}")


def main():
    score = get_score()
    grade = calculate_grade(score)
    display_results(score, grade)


if __name__ == "__main__":
    main()