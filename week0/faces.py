def main():
    # Get input from the user
    text = input()

    # Convert and print the result
    print(convert(text))


def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    return text.replace(":)", "🙂").replace(":(", "🙁")


if __name__ == "__main__":
    main()
