def main():
    print("Program that reads a year from the user and tells whether it is a leap year or not.")
    
    year = input("Enter a year: ")
    try:
        year = int(year)
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return  

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == '__main__':
    main()
