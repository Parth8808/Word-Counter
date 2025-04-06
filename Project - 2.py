def count_words(text):
    """
    This function takes a string input and returns the number of words.
    Words are assumed to be separated by whitespace.
    """
    words = text.strip().split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    print("Please enter a sentence or a paragraph below.\n")

    # Get user input
    user_input = input("Enter your text: ")

    # Error handling for empty input
    if not user_input.strip():
        print("\nError: You entered an empty string. Please try again with some text.")
        return

    # Count words
    word_count = count_words(user_input)

    # Display the result
    print(f"\nYour input contains {word_count} word(s).")

if __name__ == "__main__":
    main()
