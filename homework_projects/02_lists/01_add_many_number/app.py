def main():
    print("This program adds multiple numbers together.")
    
    add_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = 0
    
    for number in add_list:
        total += number
        print(f"Adding {number}: Current total = {total}")

    print(f"\nThe final total is {total}")

if __name__ == "__main__":
    main()
