def main():

    try:
        print("This program converts feet to inches.")
        feet=int(input("enter the number of feet: "))
        inches=feet*12
        print(f"{feet} feet = {inches} inches.")   
    except ValueError:
        print("Invalid input! Please enter a valid number for feet.")

if __name__ == "__main__":
    main()