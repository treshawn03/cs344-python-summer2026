def analyze_text(text):
    """Returns text statistics."""

    char_count = len(text)
    words = text.split()
    word_count = len(words)
    e_count = text.lower().count("e")

    return {
        "characters": char_count,
        "words": word_count,
        "e_count": e_count
    }


def main():
    text = input("Enter a line of text: ")

    stats = analyze_text(text)

    print("\nText Statistics")
    print("----------------")
    print("Characters:", stats["characters"])
    print("Words:", stats["words"])
    print("Number of 'e' letters:", stats["e_count"])


if __name__ == "__main__":
    main()