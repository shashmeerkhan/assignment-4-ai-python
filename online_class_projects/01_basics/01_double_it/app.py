def main():
    user_input = int(input("Enter a number that you want to double: "))
    curr_value = user_input * 2

    while curr_value < 100:
        print(curr_value, end=" ")
        curr_value = curr_value * 2

    print(curr_value)  # Final value that is 100 or more

if __name__ == "__main__":
    main()
