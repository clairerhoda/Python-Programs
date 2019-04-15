#Claire Rhoda
#1068768
#Program Set 1
#This program carryies out a portion of tasks for a list of intergers.

#Define constant variables.
ONE_TEN = [1,2,3,4,5,6,7,8,9,10]

def main():
    print("The original data for all functions is: ", ONE_TEN)

    #a. Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swapFirstLast(data)
    print("After swapping first and last: ",data)

    #b. Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shiftRight(data)
    print("After shifting right: ", data)

    #c. Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replaceEven(data)
    print("After replacing even elements with zero: ", data)

    #d. Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replaceNeighbors(data)
    print("After replacing with neighbors: ",data)

    #e. Demonstrate removing the middle element.
    data = list(ONE_TEN)
    removeMiddle(data)
    print("After removing the middle element(s): ", data)

    #f. Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    evenToFront(data)
    print("After moving even elements: ", data)

    #g. Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicates(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))
    
    
