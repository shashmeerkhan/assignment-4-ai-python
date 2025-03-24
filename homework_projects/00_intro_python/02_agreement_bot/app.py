def main():
    try:
        print("This program calculates the square of a number.")
        num = float(input("Enter a number: "))  
        square = num ** 2
        print(f"The square of {num} = {square:.2f}") 
    except ValueError:
        print("Invalid input. Please enter a valid number.")  

if __name__ == "__main__":
    main()
