months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip()

        # Format 1: M/D/YYYY (e.g., 8/9/1636)
        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                # Validate month and day bounds
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except ValueError:
                pass

        # Format 2: Month Day, Year (e.g., January 1, 1970)
        elif "," in date:
            try:
                # Remove comma and split into components
                date_clean = date.replace(",", "")
                month_str, day_str, year_str = date_clean.split()

                month_str = month_str.title()
                if month_str in months:
                    month = months.index(month_str) + 1
                    day = int(day_str)
                    year = int(year_str)

                    # Validate day bounds
                    if 1 <= day <= 31:
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break
            except ValueError:
                pass


if __name__ == "__main__":
    main()
