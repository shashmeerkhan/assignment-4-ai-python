def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False
def main():
    # Test the function with a sample input
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(n, low, high):
        print(f"{n} is in range [{low}, {high}]")
    else:
        print(f"{n} is not in range [{low}, {high}]")
if __name__ == '__main__':
    main()