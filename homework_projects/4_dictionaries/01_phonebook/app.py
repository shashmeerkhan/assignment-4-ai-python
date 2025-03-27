def get_phone_book():
    phone_book = {}
    while True:
        name = input("Enter your name (Press Enter to quit): ")
        if name == "":
            break
        number = input("Enter your number: ")
        phone_book[name] = number
        print(f"Added {name} with number {number}")
    return phone_book

def save_phone_book(phone_book):
    with open("phone_book.txt", "w") as file:
        for name, number in phone_book.items():
            file.write(f"{name},{number}\n")
    print("Phone book saved successfully.")

def main():
    phone_book = get_phone_book()
    print(phone_book)

    name = input("Enter a name to search: ")
    if name in phone_book:
        print(f"{name} has the number {phone_book[name]}.")
    else:
        print(f"{name} is not in the phone book.")
        add_number = input("Do you want to add this person to the phone book? (Y/N): ").lower()
        if add_number == "y":
            number = input("Enter the number: ")
            phone_book[name] = number
            print(f"{name} has been added to the phone book with the number {number}.")
        else:
            print("Okay. Have a nice day!")

    print(phone_book)
    save_phone_book(phone_book)

if __name__ == "__main__":
    main()
