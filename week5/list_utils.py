def filter_and_summarize(numbers):
    """Filters positive numbers and returns summary statistics."""

    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)

    count = len(positive_numbers)
    total = sum(positive_numbers)

    if count > 0:
        average = total / count
    else:
        average = 0

    return {
        "positive_numbers": positive_numbers,
        "count": count,
        "sum": total,
        "average": average
    }


def main():
    numbers = [12, -5, 0, 8, -2, 15, 4]

    results = filter_and_summarize(numbers)

    print("Original list:", numbers)
    print("Positive numbers:", results["positive_numbers"])
    print("Count:", results["count"])
    print("Sum:", results["sum"])
    print("Average:", results["average"])


if __name__ == "__main__":
    main()