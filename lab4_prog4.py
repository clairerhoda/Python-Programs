#Claire Rhoda
#1068768
#Program 4
#This program creates a tuple with descending positive numbers.
def getTuple()->tuple:
    """recieves tuple"""
    user_tuple = (-10,1,2,-9,3,4,-8,5,6)  #tuple is given to main func
    return user_tuple

def getNewTuple(user_tuple:tuple)->tuple:
    user_list = list(user_tuple) #tuples are immutiable so it becomes a list
    for num in user_list:
        if num <= 0:  #negative numbers are removed from list
            user_list.remove(num)
    user_list.sort()  #sorts the numbers from low to high
    user_list.reverse()  #makes the numbers descend
    user_tuple = tuple(user_list)   #list is converted back to a tuple
    return user_tuple
    
    
def main():
    user_tuple = getTuple()  #tuple is called from getTuple func
    print("Original Tuple:",user_tuple)
    print("New Tuple with Postive numbers:",getNewTuple(user_tuple))

if __name__ =="__main__":
    main()
input("\nPress enter to quit")

##Test Case 
##>>> 
##====== RESTART: /Users/clairerhoda/workspace/comp_sci_10/lab4_prog4.py ======
##Original Tuple: (-10, 1, 2, -9, 3, 4, -8, 5, 6)
##New Tuple with Postive numbers: (6, 5, 4, 3, 2, 1)
##
##Press enter to quit
##>>> 
