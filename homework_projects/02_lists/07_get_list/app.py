def print_list(lst):
    
    if lst:  
        print("Here your list:", lst)  
        
    else:
        print("The list is empty.")

def get_lst():
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
    print_list(lst)

if __name__ == "__main__":
    main()
