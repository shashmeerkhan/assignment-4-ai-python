def tall_enough_extension():
    print("Welcome to the ride height checker!")
    minimum_height = 50  # Minimum height requirement

    while True:
        height = input("How tall are you? (Press Enter to quit) ")

        if height == "":  # Exit if the user enters nothing
            print("Exiting program. Have a great day!")
            break

        try:
            height = int(height)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue  # Ask again

        if height >= minimum_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    tall_enough_extension()
