def main():
    # Menu dictionary with prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00

    while True:
        try:
            # Get input and normalize capitalization (e.g., "nachos" -> "Nachos")
            item = input("Item: ").title()

            # Check if item exists in the menu
            if item in menu:
                total += menu[item]
                # Format total to always show two decimal places
                print(f"Total: ${total:.2f}")

        except EOFError:
            # Print a newline when user presses Ctrl+D to exit cleanly
            print()
            break


if __name__ == "__main__":
    main()
