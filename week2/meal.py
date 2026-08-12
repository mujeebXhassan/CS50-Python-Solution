def main():
    # Prompt the user for the time
    time = input("What time is it? ")

    # Convert the string time into a float
    converted_time = convert(time)

    # Check which meal time it is
    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

def convert(time):
    # Split the time into hours and minutes based on the colon
    hours, minutes = time.split(":")

    # Convert both to floats and calculate the decimal hour
    # 30 minutes / 60 = 0.5 hours
    return float(hours) + (float(minutes) / 60)

if __name__ == "__main__":
    main()
