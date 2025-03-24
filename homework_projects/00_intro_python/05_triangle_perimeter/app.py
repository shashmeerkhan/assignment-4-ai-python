def main():
    print("This program calculates the perimeter of a triangle.")
    
    # Get user input safely
    try:
        side1: float = float(input("What is the length of side 1? "))
        side2: float = float(input("What is the length of side 2? "))
        side3: float = float(input("What is the length of side 3? "))

        # Calculate the perimeter
        perimeter = side1 + side2 + side3

      
        print(f"The perimeter of the triangle is {perimeter:.2f}.")
        
    except ValueError:
        print("Invalid input! Please enter a numeric side length.")


if __name__ == "__main__":
    main()
