import random

def main():
    NUM_SIDE = 6
    print(" This program simulates rolling a pair of dice.")
    die1 = random.randint(1, NUM_SIDE)
    die2 = random.randint(1, NUM_SIDE)
    print("Dice have", NUM_SIDE, "sides each.")
    print(f"You rolled a {die1} and a {die2}.")
    print("The sum of your roll is", die1 + die2)


if __name__ == "__main__":
    main()