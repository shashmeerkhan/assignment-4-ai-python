def get_user_numbers():
    print("This program counts the number of times each number appears in a list.")
    print("It uses a dictionary to keep track of the information.")

    user_numbers = []  # List to store user input

    while True:
        number = input("Enter a number (Press Enter to quit): ")

        if number == "":  # Stop if input is empty
            break
        
        try:
            number = int(number)  # Convert input to integer
        except ValueError:  
            print("Invalid input. Please enter a numeric value.")
            continue  # Skip to next iteration
        
        user_numbers.append(number)  # Add number to list

    return user_numbers

def count_numbers(user_numbers):
    number_count = {}  # Dictionary to count occurrences

    for number in user_numbers:
        if number in number_count:
            number_count[number] += 1
        else:
            number_count[number] = 1

    return number_count

def display_results(number_count):
    print("\nNumber\tCount")
    print("------\t-----")
    
    for number, count in number_count.items():
     print(str(number) + " appears " + str(count) + " times.")


def main():
    user_numbers = get_user_numbers()
    number_count = count_numbers(user_numbers)
    display_results(number_count)
    print("\nThanks for using the program!")

if __name__ == '__main__':
    main()
