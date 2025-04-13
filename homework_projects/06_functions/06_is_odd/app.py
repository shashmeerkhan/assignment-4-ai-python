def is_odd(n):
    """Return True if n is odd, False otherwise."""
    # Your code here
    return n % 2 != 0
def main():
    for i in range(10):
        if is_odd(i):
            print(f" {i} odd")
        else:
            print(f" {i} even")
            


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()