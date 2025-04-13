def main():
    fruit_list=['apple', 'banana', 'orange', 'grape', 'pineapple']
    fruit_list.append('mango')
    lst_length = len(fruit_list)
    print(lst_length)
    for fruit in fruit_list:
       print(fruit, end=" ")

if __name__=="__main__":
    main()
