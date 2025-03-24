def main():
    print("This program calculates the energy of an object using Einstein's famous equation: E = mc².")

    # Get user input for mass
    try:
        mass = float(input("Enter the mass of the object (in kg): "))
        C = 299792458  # Speed of light in meters per second

        # Calculate energy
        energy = mass * C ** 2  # Corrected formula

        # Display the result
        print(f"\nThe energy of the object is {energy} Joules.")    
        print("\nEquation used: E = m * C²")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for mass.")

if __name__ == "__main__":
    main()
