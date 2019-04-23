#Claire Rhoda
#1068768
#Program Set 1
#This program carryies out a portion of tasks for a list of intergers.

#Define constant variables.
ONE_TEN = [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]


def swapFirstLast(origData:list)->list:
    origData[0],origData[-1] = origData[-1],origData[0]
    return origData


def shiftRight(origData:list)->list:
    last = origData[-1]
    origData.insert(0,last)
    origData.reverse()
    origData.remove(last)
    origData.reverse()
    return origData


def replaceEven(origData:list)->list:
    for index in origData:
        if index % 2 == 0:
            return origData
            
            
def relaceNeighbors(origData:list)->list:
    for index in origData:
        if origData[i] > origData[n]:
            return origData


def removeMiddle(origData:list)->list:
    return
def evenToFront(origData:list)->list:
    return
def secondLargest(origData:list)->int:
    i = 0
    z = 0
    for num in origData:
        if i < num:
            z = i
            i = num
           
        if num > z and num < i:
            z = num
    return z


def isIncreasing(origData:list)->bool:
    flag = 0
    i = 1
    while i < len(origList):
        if (origList[i] < origList[i - 1]):
                return False
        i += 1
        
        else:
                return True
    return False
def hasAdjacentDuplicates(origData:list)->bool:
    return
def hasDuplicate(origData:list)->bool:
    duplicateList = []
    for num in origData:
            if num not in duplicateList:
                return True
    return False
        
    
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

    g. Demonstrate finding the second largest value.
    print("The second largest value is: ", secondLargest(ONE_TEN))

    #h. Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", isIncreasing(ONE_TEN))

    #i. Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", hasAdjacentDuplicates(ONE_TEN))

    #j. Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))
    
    
if __name__ == "__main__":
    main()
