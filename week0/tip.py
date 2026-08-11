def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the '$' sign and convert the string to a float
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Remove the '%' sign, convert to float, and divide by 100 to get a decimal
    return float(p.replace("%", "")) / 100


if __name__ == "__main__":
    main()
