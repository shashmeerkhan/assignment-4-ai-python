def print_ones_digit(n: int):
    """
    Print the ones digit of a number.
    """
    ones_digit = n % 10
    print("The ones digit is:", ones_digit)

def main():
    # Test the function with a sample input
    n = int(input("Enter a positive integer: "))
    print_ones_digit(n)

if __name__ == '__main__':
    main()
