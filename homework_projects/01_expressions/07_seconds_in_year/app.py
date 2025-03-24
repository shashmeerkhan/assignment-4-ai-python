def main():
    print("This program calculates the number of seconds in a year.")
    
    try:
        seconds_per_minute = 60
        minutes_per_hour = 60
        hours_per_day = 24
        days_per_year = 365
        seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day
        seconds_in_year = seconds_per_day * days_per_year
        print(f"There are {seconds_in_year} seconds in a year.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


if __name__ == "__main__":
    main()

