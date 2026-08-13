def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Check if the length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Check if the first two characters are letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: Check if the string contains any punctuation or spaces
    if not s.isalnum():
        return False

    # Rules 4 & 5: Check number placement and the '0' rule
    for i in range(len(s)):
        # Find the first character that is a number
        if s[i].isdigit():
            # If the very first number is a '0', it's invalid
            if s[i] == '0':
                return False

            # If there are letters *after* this number, it's invalid
            # We slice the string from the current index 'i' to the end
            if not s[i:].isdigit():
                return False

            # If it passes the number checks, we can stop checking
            break

    # If all tests pass, the plate is valid
    return True

if __name__ == "__main__":
    main()
