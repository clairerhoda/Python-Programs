#Claire Rhoda
#1068768
#Program 3
#This program removes duplicates from an user inputed list
def createList()->list:
    """user appends numbers to a list"""
    user_list = []  #blank list is formatted 
    again = 'Y'
    while again.upper() =='Y':  #allows user to enter another number to the list
        num = int(input("Enter a number"))
        user_list.append(num)
        print("Do you want to enter another number?")
        again = input("y = yes or n = no")
    return user_list  #full list is returned to main function
def removeDuplicates(user_list:list)->list:
    """duplicates are removed"""
    no_duplicate_list = [] #new list is created
    for numbers in user_list:
        if numbers not in no_duplicate_list: #duplicates are filtered out from
            no_duplicate_list.append(numbers) #original list
    return no_duplicate_list #new list is returned to main function


def main():
    """calls functions for info and displays results"""
    user_input = createList()  #new list is created from call
    print("Original List:", user_input)
    print("List after removing duplicates:", removeDuplicates(user_input))
    #new duplicate free list is printed


if __name__ =="__main__":
    main()

input("\nPress enter to exit")


##Test Case 1
##>>>
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog3.py ======
##Enter a number3
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number5
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number34
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number6
##Do you want to enter another number?
##y = yes or n = non
##Original List: [3, 5, 34, 6]
##List after removing duplicates: [3, 5, 34, 6]
##
##Test Case 2
##>>>
##Press enter to exit
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog3.py ======
##Enter a number2
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number5
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number2
##Do you want to enter another number?
##y = yes or n = non
##Original List: [2, 5, 2]
##List after removing duplicates: [2, 5]
##
##Press enter to exit
##
##Test Case 3
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog3.py ======
##Enter a number567
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number765
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number567
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number1
##Do you want to enter another number?
##y = yes or n = noy
##Enter a number309
##Do you want to enter another number?
##y = yes or n = non
##Original List: [567, 765, 567, 1, 309]
##List after removing duplicates: [567, 765, 1, 309]
##
##Press enter to exit
##>>> 
