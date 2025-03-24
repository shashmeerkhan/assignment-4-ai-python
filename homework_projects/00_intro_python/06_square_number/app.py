def main():
    try:
       print("This program calculates the square of a number.")
       num = float(input("Enter a number: "))
       square = num ** 2
       print(f"The square of {num} = {square}")
    except ValueError:
           print("Invalid input. Please enter a valid integer.")



if __name__ == "__main__":
    main()