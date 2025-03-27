def get_last_element(lst):
    
    if lst:  
        print("Last element:", lst[-1])  
        
    else:
        print("The list is empty.")

def get_lst():
    """Takes user input to create a list."""
    lst = []
    
    while True:
        elem = input("Enter an element (press Enter without input to stop): ")
        if elem == "":  
            break
        lst.append(elem)
      
    return lst

def main():
    """Main function to get a list and print its last element."""
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":
    main()
