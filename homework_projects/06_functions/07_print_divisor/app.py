def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor, end=" ")
def main():
    # Test the function with a sample input
    n = input("Enter a positive integer: ")
    print_divisors(int(n))
    
if __name__ == '__main__':
    main()