import math  # Importing math library for square root calculation

def main():
    print("This program calculates the hypotenuse of a right triangle using the Pythagorean theorem.")
    
    try:
        side1 = float(input("Enter the length of AB: "))
        side2 = float(input("Enter the length of BC: "))
        
        if side1 <= 0 or side2 <= 0:
            print("Side lengths must be positive numbers.")
            return
        
        hypotenuse = math.sqrt(side1**2 + side2**2)
        print(f"The length of AC (hypotenuse) is: {hypotenuse:.2f}")
    
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    main()
