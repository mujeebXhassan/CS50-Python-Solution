def main():
    while True:
        fraction = input("Fraction: ")
        try:
            # Split input string into numerator (x) and denominator (y)
            x_str, y_str = fraction.split("/")
            x = int(x_str)
            y = int(y_str)

            # Reject negative numbers or cases where X > Y
            if x < 0 or y < 0 or x > y:
                continue

            # Calculate percentage rounded to nearest integer
            percentage = round((x / y) * 100)
            break

        except (ValueError, ZeroDivisionError):
            # Reprompt if inputs are not integers or denominator is 0
            pass

    # Print gauge result based on percentage threshold
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
