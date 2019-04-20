#Claire Rhoda
#1068768
#Program 8
#This program allows the user to modify a coffee record.

def main():
    answer = 'Y'
    while answer.upper() == 'Y':
        print("Coffee Menu")
        print("------------")
        f = open('coffee.txt','r')
        file_contents = f.read()
        print(file_contents)
        f.close()
        print("1. Search")
        print("2. Delete")
        print("3. Show Information")
        print("4. Modify")
        print("5. Add")
        choice = input("Please choose a program from the list above")
        if choice == '1':
            import search_coffee_records
            search_coffee_records.search()
        if choice == '2':
            import delete_coffee_record
            delete_coffee_record.del_coffee()

        if choice == '3':
            import show_coffee_records
            show_coffee_records.show()

        if choice == '4':
            import modify_coffee_records
            modify_coffee_records.mod_coffee()

        if choice == '5':
            import add_coffee_record
            add_coffee_record.add_coffee()
        print("Would you like to make any more changes or look up ",end='')
        print("another item?")
        answer = input("Enter 'y' for yes or anything else for no")


if  __name__ == "__main__":
    main()
