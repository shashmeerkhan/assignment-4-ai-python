import random

def main():
    guess_num = random.randint(1, 99)
    
    while True:
        user_input = int(input("Enter a positive integer number: "))
        
        if user_input < guess_num:
            print("Your guess is too low.")
        elif user_input > guess_num:
            print("Your guess is too high.")
        else:
            print("Congrats! The number was: " + str(guess_num))
            break

if __name__ == "__main__":
    main()
