def get_first_element(lst):
    if lst:  # Check if the list is not empty
        print("First element:", lst[0])
    else:
        print("The list is empty. No first element.")

def get_lst():
    lst = []
    print("Enter elements (press Enter without input to stop):")
    while True:
        elem = input("Enter an element (press Enter without input to stop): ")
        if elem == "":  
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == "__main__":
    main()
