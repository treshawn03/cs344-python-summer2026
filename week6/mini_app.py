def read_grades(filename):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                # Skip empty lines so they do not cause errors
                if not line:
                    continue

                parts = line.split(",")

                # Skip lines that do not have both a name and a grade
                if len(parts) != 2:
                    print("Warning: Skipping invalid line:", line)
                    continue

                name = parts[0]
                grade_text = parts[1]

                try:
                    grade = int(grade_text)
                except ValueError:
                    print("Warning: Invalid grade for", name)
                    continue

                students.append((name, grade))

        return students

    except FileNotFoundError:
        print("Error: The file was not found.")
        return []


def print_report(students):
    if not students:
        print("No student data available.")
        return

    grades = []

    for student in students:
        grades.append(student[1])

    total_students = len(grades)
    average = sum(grades) / total_students
    highest = max(grades)
    lowest = min(grades)

    print("\n----- Grade Report -----")
    print("Students:", total_students)
    print(f"Average Grade: {average:.2f}")
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)


students = read_grades("grades.txt")
print_report(students)