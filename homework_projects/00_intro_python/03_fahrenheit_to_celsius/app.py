def main():
    print("This program converts Fahrenheit to Celsius.")
    
    # Get user input safely
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))  
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        print(f"Temperature {fahrenheit}°F = {celsius:.2f}°C.")
    except ValueError:
        print("Invalid input! Please enter a numeric temperature.")

if __name__ == "__main__":
    main()
