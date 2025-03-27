# Define voting age for each country
voting_age_Peturksbouipo = 16
voting_age_Stanlau = 25
voting_age_Mayengua = 48

def can_vote(age):
    """Determines in which countries the user can vote based on their age."""
    if age >= voting_age_Mayengua:
        print(f"You can vote in Peturksbouipo, Stanlau, and Mayengua (voting ages: 16, 25, and 48).")
    elif age >= voting_age_Stanlau:
        print(f"You can vote in Peturksbouipo and Stanlau (voting ages: 16 and 25). You cannot vote in Mayengua.")
    elif age >= voting_age_Peturksbouipo:
        print(f"You can vote in Peturksbouipo (voting age: 16). You cannot vote in Stanlau or Mayengua.")
    else:
        print(f"You cannot vote in Peturksbouipo, Stanlau, or Mayengua (voting ages: 16, 25, and 48).")

def main():
    """Main function to get user input and check voting eligibility."""
    print("This program checks if you can vote in different countries.")
    age = int(input("Enter your age: "))  
    can_vote(age)  

if __name__ == '__main__':
    main()
