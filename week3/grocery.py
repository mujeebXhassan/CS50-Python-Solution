def main():
    grocery_list = {}

    while True:
        try:
            # Prompt for item and convert to uppercase
            item = input().upper().strip()

            # Track quantity for each item
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            # Print a blank line and stop looping when user presses Ctrl+D
            print()
            break

    # Sort items alphabetically and display count with item name
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()
