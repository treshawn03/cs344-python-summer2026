def count_words(text):
    """Counts how many times each word appears."""

    # Convert all text to lowercase
    text = text.lower()

    # Split the text into words
    words = text.split()

    # Dictionary to store word counts
    word_counts = {}

    # Count each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def main():
    text = input("Enter a line or paragraph of text: ")

    counts = count_words(text)

    print("\nWord Frequency")
    print("--------------")

    for word, count in counts.items():
        print(f"{word}: {count}")


# Fixed formatting issue when printing word counts.
if __name__ == "__main__":
    main()