def main():
    fruits = {"apple":400, "banana": 200, "orange": 500, "pear": 1000, "grape": 450}  
    total_cost = 0
    
    for fruit_name, fruit_price in fruits.items(): 
        try:
            amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
            cost = fruit_price * amount_bought
            total_cost += cost
            print(f"Cost of {amount_bought} {fruit_name}(s) is {cost}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Total cost is {total_cost}.")
    print("Thank you for shopping with us!")

if __name__ == '__main__':
    main()
