def main():
    print("This program calculates the remainder of a division operation.")
    
    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        if divisor == 0:
            print("Error! Division by zero is not allowed.")
            return
        
        remainder = dividend % divisor
        quotient = dividend // divisor
        
        print(f"The result of this division is {quotient} with a remainder of {remainder}.")
    
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
