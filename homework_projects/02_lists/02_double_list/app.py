def main():
    print("This program doubles each element in a list of numbers.")

    my_list = [1, 2, 3, 4]
    double_list = []

    print(f"The original list is: {my_list}")

    for number in my_list:  
        double_list.append(number * 2)

    print(f"The doubled list is: {double_list}")

if __name__ == "__main__":
    main()
