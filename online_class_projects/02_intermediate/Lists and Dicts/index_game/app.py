def index_game():
    my_list = [1, 2, 3, 4, 5]
    print("Current list:", my_list)

    print("What do you want to do?")
    print("1. Access an item")
    print("2. Change an item")
    print("3. Get a part of the list")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        index = int(input("Enter index to access: "))
        if index < len(my_list):
            print("Item at index", index, "is", my_list[index])
        else:
            print("Index out of range.")

    elif choice == "2":
        index = int(input("Enter index to change: "))
        if index < len(my_list):
            new_value = input("Enter new value: ")
            my_list[index] = new_value
            print("Updated list:", my_list)
        else:
            print("Index out of range.")

    elif choice == "3":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", my_list[start:end])

    else:
        print("Invalid choice.")

index_game()
