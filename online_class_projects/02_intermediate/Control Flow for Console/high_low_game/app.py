import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    your_score=0
    for i in range(NUM_ROUNDS):
        print("Round", i+1)
        computer_num=random.randint(1,100)
        your_num=random.randint(1,100)
        print("Your number is ", your_num)
        choice=input("Do you think your number is higher or lower than the computer's number?  ")
        higher_and_correct=choice=="higher" and your_num>computer_num
        lower_and_correct=choice=="lower" and your_num<computer_num

        if higher_and_correct or lower_and_correct:
            print("you were right ! The computer's number was ", computer_num)
            your_score+=1
        else:
            print("Aww, that's incorrect.The computer's number was ", computer_num)
        print(" your score is now ", your_score)
        print()
    print("Thank for playing!")
if __name__ == "__main__":
    main()